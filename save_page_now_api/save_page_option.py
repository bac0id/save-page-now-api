class SavePageOption:
    def __init__(
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
    ):
        self.url: str = url
        self.save_outlinks = save_outlinks
        self.save_errors = save_errors
        self.save_screenshot = save_screenshot
        self.enable_adblocker = enable_adblocker
        self.save_in_my_web_archive = save_in_my_web_archive
        self.email_me_result = email_me_result
        self.email_me_wacz_file_with_the_results = (
            email_me_wacz_file_with_the_results
        )

    def to_http_post_payload(self):
        payload = {"url": self.url}
        if self.save_outlinks:
            payload["capture_outlinks"] = "1"
        if self.save_errors:
            payload["capture_all"] = "on"
        if self.save_screenshot:
            payload["capture_screenshot"] = "on"
        if not self.enable_adblocker:  # if disable ad blocker
            payload["disable_adblocker"] = "on"
        if self.save_in_my_web_archive:
            payload["wm-save-mywebarchive"] = "on"
        if self.email_me_result:
            payload["email_result"] = "on"
        if self.email_me_wacz_file_with_the_results:
            payload["wacz"] = "on"
        return payload
