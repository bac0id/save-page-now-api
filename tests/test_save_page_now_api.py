import unittest
from unittest.mock import Mock, patch
from urllib.parse import urljoin

from requests.exceptions import HTTPError, JSONDecodeError

from save_page_now_api import (
    ERROR_CODE_TO_EXCEPTION,
    SavePageNowApi,
    SavePageNowBadRequestError,
    SavePageNowError,
    SavePageNowNotFoundError,
    SavePageOption,
)


class TestSavePageNowApi(unittest.TestCase):
    """Unit tests for the SavePageNowApi class."""

    def setUp(self):
        """Set up a SavePageNowApi instance and common mocks before each test."""
        self.token = "test_token"
        self.user_agent = "test_user_agent"
        self.api = SavePageNowApi(token=self.token, user_agent=self.user_agent)
        self.test_url = "http://example.com"

        # Mock the requests.post method globally for all tests in this class
        self.patcher = patch("requests.post")
        self.mock_post = self.patcher.start()

        # Set up a default successful mock response
        self.mock_response = Mock()
        self.mock_response.status_code = 200
        self.mock_response.json.return_value = {
            "url": self.test_url,
            "job_id": "test_job_id",
            "status": "success",
            "timestamp": "2023-01-01T10:00:00Z",
            "status_ext": "success:capture-finished",
            "wayback_url": f"https://web.archive.org/web/timestamp/{self.test_url}",
        }
        # Ensure raise_for_status does nothing on success (status_code 200)
        self.mock_response.raise_for_status.return_value = None
        self.mock_post.return_value = self.mock_response

    def tearDown(self):
        """Stop the patcher after each test."""
        self.patcher.stop()

    def test_get_save_api_url_default_host(self):
        """Test __get_save_api_url with the default host."""
        expected_url = urljoin(
            SavePageNowApi.DEFAULT_USER_AGENT, "/save"
        )  # Corrected: use default host, not default user agent
        expected_url = urljoin("https://web.archive.org/", "/save")
        self.assertEqual(
            self.api._SavePageNowApi__get_save_api_url(), expected_url
        )

    def test_get_save_api_url_custom_host(self):
        """Test __get_save_api_url with a custom host."""
        custom_host = "https://web.archivep75mbjunhxc6x4j5mwjmomyxb573v42baldlqu56ruil2oiad.onion/"
        custom_api = SavePageNowApi(token=self.token, host=custom_host)
        expected_url = urljoin(custom_host, "/save")
        self.assertEqual(
            custom_api._SavePageNowApi__get_save_api_url(), expected_url
        )

    def test_get_save_api_url_host_without_trailing_slash(self):
        """Test __get_save_api_url with a custom host without a trailing slash."""
        custom_host = "https://web.archivep75mbjunhxc6x4j5mwjmomyxb573v42baldlqu56ruil2oiad.onion"  # No trailing slash
        custom_api = SavePageNowApi(token=self.token, host=custom_host)
        # urljoin should handle the missing slash correctly
        expected_url = urljoin(custom_host, "/save")
        self.assertEqual(
            custom_api._SavePageNowApi__get_save_api_url(), expected_url
        )

    def test_save_success(self):
        """Test a successful save operation."""
        result = self.api.save(self.test_url)

        # Assert that requests.post was called correctly
        expected_headers = {
            "Accept": "application/json",
            "User-Agent": self.user_agent,
            "Authorization": f"LOW {self.token}",
        }
        option = SavePageOption(url=self.test_url)
        expected_payload = option.to_http_post_payload()

        self.mock_post.assert_called_once_with(
            url=self.api._SavePageNowApi__get_save_api_url(),
            headers=expected_headers,
            data=expected_payload,
            proxies=None,
        )

        # Assert that the correct result was returned
        self.assertEqual(result, self.mock_response.json.return_value)
        self.mock_response.raise_for_status.assert_called_once()  # Ensure status was checked

    def test_save_with_options(self):
        """Test saving with various options enabled."""
        options = {
            "save_outlinks": True,
            "save_errors": True,
            "save_screenshot": True,
            "enable_adblocker": False,  # This means disable_adblocker=on
            "save_in_my_web_archive": True,
            "email_me_result": True,
            "email_me_wacz_file_with_the_results": True,
        }
        self.api.save(self.test_url, **options)

        # Assert that requests.post was called with the correct payload based on options
        expected_payload = {
            "url": self.test_url,
            "capture_outlinks": "1",
            "capture_all": "on",
            "capture_screenshot": "on",
            "disable_adblocker": "on",
            "wm-save-mywebarchive": "on",
            "email_result": "on",
            "wacz": "on",
        }

        self.mock_post.assert_called_once_with(
            url=self.api._SavePageNowApi__get_save_api_url(),
            headers=self.api._SavePageNowApi__get_http_headers(),
            data=expected_payload,
            proxies=None,
        )

    def test_save_http_error(self):
        """Test handling of non-2xx HTTP status codes."""
        self.mock_response.status_code = 404
        # Configure raise_for_status to raise an HTTPError
        self.mock_response.raise_for_status.side_effect = HTTPError("Not Found")

        with self.assertRaises(HTTPError) as cm:
            self.api.save(self.test_url)

        # Assert that raise_for_status was called
        self.mock_response.raise_for_status.assert_called_once()
        # Assert that the correct exception was raised
        self.assertIn("Not Found", str(cm.exception))

    def test_save_json_decode_error(self):
        """Test handling of invalid JSON response."""
        self.mock_response.status_code = 200  # Still a successful HTTP status
        # Configure json() to raise a JSONDecodeError
        self.mock_response.json.side_effect = JSONDecodeError(
            "Invalid JSON", "doc", 0
        )

        with self.assertRaises(JSONDecodeError) as cm:
            self.api.save(self.test_url)

        # Assert that json() was called and raised the error
        self.mock_response.json.assert_called_once()
        # Assert that raise_for_status was also called (as per __get_json logic)
        self.mock_response.raise_for_status.assert_called()
        self.assertIn("Invalid JSON", str(cm.exception))

    def test_save_api_error_specific(self):
        """Test handling of a specific API error from status_ext."""
        error_status_ext = "error:bad-request"
        self.mock_response.json.return_value = {
            "url": self.test_url,
            "job_id": "test_job_id",
            "status": "error",
            "timestamp": "2023-01-01T10:00:00Z",
            "status_ext": error_status_ext,
        }
        # Ensure raise_for_status doesn't raise for 200 OK, but the internal logic does

        # Get the expected exception class from the mapping
        expected_exception = ERROR_CODE_TO_EXCEPTION.get(
            error_status_ext, SavePageNowError
        )

        with self.assertRaises(expected_exception) as cm:
            self.api.save(self.test_url)

        # Assert that the raised exception is an instance of the specific error class
        self.assertIsInstance(cm.exception, SavePageNowBadRequestError)
        # Assert the message contains the URL and status_ext
        self.assertIn(self.test_url, str(cm.exception))
        self.assertIn(error_status_ext, str(cm.exception))

    def test_save_api_error_unknown(self):
        """Test handling of an unknown API error status_ext."""
        error_status_ext = "error:some-new-unknown-error"
        self.mock_response.json.return_value = {
            "url": self.test_url,
            "job_id": "test_job_id",
            "status": "error",
            "timestamp": "2023-01-01T10:00:00Z",
            "status_ext": error_status_ext,
        }

        # It should raise the base SavePageNowError for unknown status_ext
        with self.assertRaises(SavePageNowError) as cm:
            self.api.save(self.test_url)

        # Assert that the raised exception is an instance of the base error class
        self.assertIsInstance(cm.exception, SavePageNowError)
        # Assert the message contains the URL and status_ext
        self.assertIn(self.test_url, str(cm.exception))
        self.assertIn(error_status_ext, str(cm.exception))

    def test_save_api_status_not_error_but_status_ext_error(self):
        """
        Test case where 'status' is not 'error', but 'status_ext' starts with 'error'.
        The logic should still raise an exception based on status_ext.
        """
        error_status_ext = "error:not-found"
        self.mock_response.json.return_value = {
            "url": self.test_url,
            "job_id": "test_job_id",
            "status": "pending",  # Status is not 'error'
            "timestamp": "2023-01-01T10:00:00Z",
            "status_ext": error_status_ext,  # But status_ext indicates an error
        }

        expected_exception = ERROR_CODE_TO_EXCEPTION.get(
            error_status_ext, SavePageNowError
        )

        with self.assertRaises(expected_exception) as cm:
            self.api.save(self.test_url)

        self.assertIsInstance(cm.exception, SavePageNowNotFoundError)
        self.assertIn(self.test_url, str(cm.exception))
        self.assertIn(error_status_ext, str(cm.exception))


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
