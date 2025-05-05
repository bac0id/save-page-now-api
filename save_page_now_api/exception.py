class SavePageNowError(Exception):
    """Base exception for SavePageNow API errors."""

    def __init__(
        self, url: str, status_ext: str, message: str = "SavePageNow API error"
    ):
        self.url = url
        self.status_ext = status_ext
        self.message = f"{message} for URL: {url} (status_ext: {status_ext})"
        super().__init__(self.message)


class SavePageNowBadRequestError(SavePageNowError):
    """Raised for error:bad-request."""

    def __init__(self, url: str, status_ext: str):
        super().__init__(
            url,
            status_ext,
            "The server could not understand the request due to invalid syntax.",
        )


class SavePageNowBadGatewayError(SavePageNowError):
    """Raised for error:bad-gateway."""

    def __init__(self, url: str, status_ext: str):
        super().__init__(url, status_ext, "Bad Gateway error.")


class SavePageNowBandwidthLimitExceededError(SavePageNowError):
    """Raised for error:bandwidth-limit-exceeded."""

    def __init__(self, url: str, status_ext: str):
        super().__init__(
            url,
            status_ext,
            "The target server has exceeded the bandwidth limit.",
        )


class SavePageNowBlockedError(SavePageNowError):
    """Raised for error:blocked."""

    def __init__(self, url: str, status_ext: str):
        super().__init__(url, status_ext, "The target site is blocking us.")


class SavePageNowBlockedClientIPError(SavePageNowError):
    """Raised for error:blocked-client-ip."""

    def __init__(self, url: str, status_ext: str):
        super().__init__(url, status_ext, "Anonymous client IP is blocked.")


class SavePageNowBlockedURLError(SavePageNowError):
    """Raised for error:blocked-url."""

    def __init__(self, url: str, status_ext: str):
        super().__init__(url, status_ext, "The URL is on a block list.")


class SavePageNowBrowseTimeoutError(SavePageNowError):
    """Raised for error:Browse-timeout."""

    def __init__(self, url: str, status_ext: str):
        super().__init__(url, status_ext, "Headless browser timeout.")


class SavePageNowCaptureLocationError(SavePageNowError):
    """Raised for error:capture-location-error."""

    def __init__(self, url: str, status_ext: str):
        super().__init__(
            url, status_ext, "Cannot find the created capture location."
        )


class SavePageNowCannotFetchError(SavePageNowError):
    """Raised for error:cannot-fetch."""

    def __init__(self, url: str, status_ext: str):
        super().__init__(
            url,
            status_ext,
            "Cannot fetch the target URL due to system overload.",
        )


class SavePageNowCeleryError(SavePageNowError):
    """Raised for error:celery."""

    def __init__(self, url: str, status_ext: str):
        super().__init__(
            url, status_ext, "Cannot start capture task (Celery error)."
        )


class SavePageNowFilesizeLimitError(SavePageNowError):
    """Raised for error:filesize-limit."""

    def __init__(self, url: str, status_ext: str):
        super().__init__(
            url, status_ext, "Cannot capture web resources over 2GB."
        )


class SavePageNowFTPAccessDeniedError(SavePageNowError):
    """Raised for error:ftp-access-denied."""

    def __init__(self, url: str, status_ext: str):
        super().__init__(
            url,
            status_ext,
            "Tried to capture an FTP resource but access was denied.",
        )


class SavePageNowGatewayTimeoutError(SavePageNowError):
    """Raised for error:gateway-timeout."""

    def __init__(self, url: str, status_ext: str):
        super().__init__(
            url, status_ext, "The target server didn't respond in time."
        )


class SavePageNowHTTPVersionNotSupportedError(SavePageNowError):
    """Raised for error:http-version-not-supported."""

    def __init__(self, url: str, status_ext: str):
        super().__init__(
            url,
            status_ext,
            "The target server does not support the HTTP protocol version.",
        )


class SavePageNowInternalAPIError(SavePageNowError):
    """Raised for error:internal-server-error."""

    def __init__(self, url: str, status_ext: str):
        super().__init__(url, status_ext, "SPN internal server error.")


class SavePageNowInvalidURLSyntaxError(SavePageNowError):
    """Raised for error:invalid-url-syntax."""

    def __init__(self, url: str, status_ext: str):
        super().__init__(url, status_ext, "Target URL syntax is not valid.")


class SavePageNowInvalidServerResponseError(SavePageNowError):
    """Raised for error:invalid-server-response."""

    def __init__(self, url: str, status_ext: str):
        super().__init__(
            url, status_ext, "The target server response was invalid."
        )


class SavePageNowInvalidHostResolutionError(SavePageNowError):
    """Raised for error:invalid-host-resolution."""

    def __init__(self, url: str, status_ext: str):
        super().__init__(url, status_ext, "Couldn’t resolve the target host.")


class SavePageNowJobFailedError(SavePageNowError):
    """Raised for error:job-failed."""

    def __init__(self, url: str, status_ext: str):
        super().__init__(url, status_ext, "Capture failed due to system error.")


class SavePageNowMethodNotAllowedError(SavePageNowError):
    """Raised for error:method-not-allowed."""

    def __init__(self, url: str, status_ext: str):
        super().__init__(
            url, status_ext, "The request method is known but disabled."
        )


class SavePageNowNotImplementedError(SavePageNowError):
    """Raised for error:not-implemented."""

    def __init__(self, url: str, status_ext: str):
        super().__init__(
            url,
            status_ext,
            "The request method is not supported by the server.",
        )


class SavePageNowNoBrowsersAvailableError(SavePageNowError):
    """Raised for error:no-browsers-available."""

    def __init__(self, url: str, status_ext: str):
        super().__init__(
            url, status_ext, "SPN2 back-end headless browser cannot run."
        )


class SavePageNowNetworkAuthenticationRequiredError(SavePageNowError):
    """Raised for error:network-authentication-required."""

    def __init__(self, url: str, status_ext: str):
        super().__init__(
            url,
            status_ext,
            "The client needs to authenticate to gain network access.",
        )


class SavePageNowNoAccessError(SavePageNowError):
    """Raised for error:no-access."""

    def __init__(self, url: str, status_ext: str):
        super().__init__(
            url, status_ext, "Target URL could not be accessed (e.g., 403)."
        )


class SavePageNowNotFoundError(SavePageNowError):
    """Raised for error:not-found."""

    def __init__(self, url: str, status_ext: str):
        super().__init__(url, status_ext, "Target URL not found (e.g., 404).")


class SavePageNowProxyError(SavePageNowError):
    """Raised for error:proxy-error."""

    def __init__(self, url: str, status_ext: str):
        super().__init__(url, status_ext, "SPN2 back-end proxy error.")


class SavePageNowProtocolError(SavePageNowError):
    """Raised for error:protocol-error."""

    def __init__(self, url: str, status_ext: str):
        super().__init__(
            url, status_ext, "HTTP connection broken (e.g., IncompleteRead)."
        )


class SavePageNowReadTimeoutError(SavePageNowError):
    """Raised for error:read-timeout."""

    def __init__(self, url: str, status_ext: str):
        super().__init__(url, status_ext, "HTTP connection read timeout.")


class SavePageNowSoftTimeLimitExceededError(SavePageNowError):
    """Raised for error:soft-time-limit-exceeded."""

    def __init__(self, url: str, status_ext: str):
        super().__init__(
            url, status_ext, "Capture duration exceeded 45s time limit."
        )


class SavePageNowServiceUnavailableError(SavePageNowError):
    """Raised for error:service-unavailable."""

    def __init__(self, url: str, status_ext: str):
        super().__init__(url, status_ext, "Service unavailable.")


class SavePageNowTooManyDailyCapturesError(SavePageNowError):
    """Raised for error:too-many-daily-captures."""

    def __init__(self, url: str, status_ext: str):
        super().__init__(
            url, status_ext, "This URL has been captured 10 times today."
        )


class SavePageNowTooManyRedirectsError(SavePageNowError):
    """Raised for error:too-many-redirects."""

    def __init__(self, url: str, status_ext: str):
        super().__init__(url, status_ext, "Too many redirects.")


class SavePageNowTooManyRequestsError(SavePageNowError):
    """Raised for error:too-many-requests."""

    def __init__(self, url: str, status_ext: str):
        super().__init__(
            url, status_ext, "The target host has received too many requests."
        )


class SavePageNowUserSessionLimitError(SavePageNowError):
    """Raised for error:user-session-limit."""

    def __init__(self, url: str, status_ext: str):
        super().__init__(
            url,
            status_ext,
            "User has reached the limit of concurrent active capture sessions.",
        )


class SavePageNowUnauthorizedError(SavePageNowError):
    """Raised for error:unauthorized."""

    def __init__(self, url: str, status_ext: str):
        super().__init__(url, status_ext, "The server requires authentication.")


# Mapping from status_ext string to Exception Class
ERROR_CODE_TO_EXCEPTION = {
    "error:bad-gateway": SavePageNowBadGatewayError,
    "error:bad-request": SavePageNowBadRequestError,
    "error:bandwidth-limit-exceeded": SavePageNowBandwidthLimitExceededError,
    "error:blocked": SavePageNowBlockedError,
    "error:blocked-client-ip": SavePageNowBlockedClientIPError,
    "error:blocked-url": SavePageNowBlockedURLError,
    "error:Browse-timeout": SavePageNowBrowseTimeoutError,
    "error:capture-location-error": SavePageNowCaptureLocationError,
    "error:cannot-fetch": SavePageNowCannotFetchError,
    "error:celery": SavePageNowCeleryError,
    "error:filesize-limit": SavePageNowFilesizeLimitError,
    "error:ftp-access-denied": SavePageNowFTPAccessDeniedError,
    "error:gateway-timeout": SavePageNowGatewayTimeoutError,
    "error:http-version-not-supported": SavePageNowHTTPVersionNotSupportedError,
    "error:internal-server-error": SavePageNowInternalAPIError,
    "error:invalid-url-syntax": SavePageNowInvalidURLSyntaxError,
    "error:invalid-server-response": SavePageNowInvalidServerResponseError,
    "error:invalid-host-resolution": SavePageNowInvalidHostResolutionError,
    "error:job-failed": SavePageNowJobFailedError,
    "error:method-not-allowed": SavePageNowMethodNotAllowedError,
    "error:not-implemented": SavePageNowNotImplementedError,  # Maps to the same class
    "error:no-browsers-available": SavePageNowNoBrowsersAvailableError,
    "error:network-authentication-required": SavePageNowNetworkAuthenticationRequiredError,
    "error:no-access": SavePageNowNoAccessError,
    "error:not-found": SavePageNowNotFoundError,
    "error:proxy-error": SavePageNowProxyError,
    "error:protocol-error": SavePageNowProtocolError,
    "error:read-timeout": SavePageNowReadTimeoutError,
    "error:soft-time-limit-exceeded": SavePageNowSoftTimeLimitExceededError,
    "error:service-unavailable": SavePageNowServiceUnavailableError,
    "error:too-many-daily-captures": SavePageNowTooManyDailyCapturesError,
    "error:too-many-redirects": SavePageNowTooManyRedirectsError,
    "error:too-many-requests": SavePageNowTooManyRequestsError,
    "error:user-session-limit": SavePageNowUserSessionLimitError,
    "error:unauthorized": SavePageNowUnauthorizedError,
}
