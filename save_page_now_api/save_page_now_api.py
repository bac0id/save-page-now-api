from urllib.parse import urljoin

import requests
from requests.exceptions import JSONDecodeError

from .exception import *
from .save_page_option import SavePageOption


class SavePageNowApi:
    DEFAULT_USER_AGENT = "save-page-now-api (https://github.com/bac0id/save-page-now-api)"

    def __init__(
        self,
        *,
        host: str = "https://web.archive.org/",
        token: str,
        user_agent: str = DEFAULT_USER_AGENT,
        proxies=None,
    ):
        self.host = host
        self.token = token
        self.user_agent = user_agent
        self.proxies = proxies

    def __get_save_api_url(self) -> str:
        api_url = urljoin(self.host, "/save")
        return api_url

    def __get_http_headers(self) -> dict[str, str]:
        headers = {
            "Accept": "application/json",
            "User-Agent": self.user_agent,
            "Authorization": f"LOW {self.token}",
        }
        return headers

    def save(
        self,
        url: str,
        *,
        save_outlinks=False,
        save_errors=True,
        save_screenshot=False,
        enable_adblocker=False,
        save_in_my_web_archive=False,
        email_me_result=False,
        email_me_wacz_file_with_the_results=False,
    ) -> dict:
        headers = self.__get_http_headers()
        option = SavePageOption(
            url=url,
            save_outlinks=save_outlinks,
            save_errors=save_errors,
            save_screenshot=save_screenshot,
            enable_adblocker=enable_adblocker,
            save_in_my_web_archive=save_in_my_web_archive,
            email_me_result=email_me_result,
            email_me_wacz_file_with_the_results=email_me_wacz_file_with_the_results,
        )
        payload = option.to_http_post_payload()

        api_url = self.__get_save_api_url()
        response = requests.post(
            url=api_url, headers=headers, data=payload, proxies=self.proxies
        )

        # raise for errors
        response.raise_for_status()
        response_json = self.__get_json(response)
        self.__raise_for_errors_in_json(url, response_json)

        return response_json

    def __get_json(self, response: requests.Response):
        try:
            response_json: dict = response.json()
        except JSONDecodeError as e:
            response.raise_for_status()
            raise e
        return response_json

    def __raise_for_errors_in_json(self, url: str, response_json: dict):
        status_ext: str = response_json.get("status_ext")
        if status_ext and status_ext.startswith("error"):
            exception_class = ERROR_CODE_TO_EXCEPTION.get(
                status_ext, SavePageNowError
            )
            # Raise the specific or base SavePageNowError
            raise exception_class(url, status_ext)
        return response_json
