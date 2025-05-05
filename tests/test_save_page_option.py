import unittest

from save_page_now_api.save_page_option import SavePageOption


class TestSavePageOption(unittest.TestCase):

    def test_init_attributes(self):
        url = "http://example.com"
        options = SavePageOption(
            url=url,
            save_outlinks=True,
            save_errors=False,
            save_screenshot=True,
            enable_adblocker=False,
            save_in_my_web_archive=True,
            email_me_result=False,
            email_me_wacz_file_with_the_results=True,
        )

        self.assertEqual(options.url, url)
        self.assertTrue(options.save_outlinks)
        self.assertFalse(options.save_errors)
        self.assertTrue(options.save_screenshot)
        self.assertFalse(options.enable_adblocker)
        self.assertTrue(options.save_in_my_web_archive)
        self.assertFalse(options.email_me_result)
        self.assertTrue(options.email_me_wacz_file_with_the_results)

    def test_to_http_post_payload_all_false(self):
        url = "http://example.com/all_false"
        options = SavePageOption(
            url=url,
            save_outlinks=False,
            save_errors=False,
            save_screenshot=False,
            enable_adblocker=True,  # adblocker enabled -> disable_adblocker should NOT be in payload
            save_in_my_web_archive=False,
            email_me_result=False,
            email_me_wacz_file_with_the_results=False,
        )
        expected_payload = {"url": url}
        self.assertEqual(options.to_http_post_payload(), expected_payload)

    def test_to_http_post_payload_all_true(self):
        url = "http://example.com/all_true"
        options = SavePageOption(
            url=url,
            save_outlinks=True,
            save_errors=True,
            save_screenshot=True,
            enable_adblocker=False,  # adblocker disabled -> disable_adblocker should be in payload
            save_in_my_web_archive=True,
            email_me_result=True,
            email_me_wacz_file_with_the_results=True,
        )
        expected_payload = {
            "url": url,
            "capture_outlinks": "1",
            "capture_all": "on",
            "capture_screenshot": "on",
            "disable_adblocker": "on",
            "wm-save-mywebarchive": "on",
            "email_result": "on",
            "wacz": "on",
        }
        self.assertEqual(options.to_http_post_payload(), expected_payload)

    def test_to_http_post_payload_mixed(self):
        url = "http://example.com/mixed"
        options = SavePageOption(
            url=url,
            save_outlinks=True,
            save_errors=False,
            save_screenshot=True,
            enable_adblocker=True,  # adblocker enabled
            save_in_my_web_archive=False,
            email_me_result=True,
            email_me_wacz_file_with_the_results=False,
        )
        expected_payload = {
            "url": url,
            "capture_outlinks": "1",
            "capture_screenshot": "on",
            # "disable_adblocker" should NOT be here because enable_adblocker is True
            "email_result": "on",
        }
        self.assertEqual(options.to_http_post_payload(), expected_payload)

    def test_to_http_post_payload_adblocker_logic(self):
        url = "http://example.com/adblock"

        # Test case 1: enable_adblocker is True (adblocker is ON)
        options_enabled = SavePageOption(
            url=url,
            save_outlinks=False,
            save_errors=False,
            save_screenshot=False,
            enable_adblocker=True,
            save_in_my_web_archive=False,
            email_me_result=False,
            email_me_wacz_file_with_the_results=False,
        )
        payload_enabled = options_enabled.to_http_post_payload()
        self.assertNotIn("disable_adblocker", payload_enabled)

        # Test case 2: enable_adblocker is False (adblocker is OFF)
        options_disabled = SavePageOption(
            url=url,
            save_outlinks=False,
            save_errors=False,
            save_screenshot=False,
            enable_adblocker=False,
            save_in_my_web_archive=False,
            email_me_result=False,
            email_me_wacz_file_with_the_results=False,
        )
        payload_disabled = options_disabled.to_http_post_payload()
        self.assertIn("disable_adblocker", payload_disabled)
        self.assertEqual(payload_disabled["disable_adblocker"], "on")


if __name__ == "__main__":
    unittest.main()
