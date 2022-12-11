"""Config flow for Destiny 2 Vendors."""
import logging

from const import DOMAIN

from homeassistant.helpers import config_entry_oauth2_flow


class OAuth2FlowHandler(
    config_entry_oauth2_flow.AbstractOAuth2FlowHandler, domain=DOMAIN
):
    """Config flow to handle Destiny 2 Vendors OAuth2 authentication."""

    DOMAIN = DOMAIN

    @property
    def logger(self) -> logging.Logger:
        """Return logger."""
        return logging.getLogger(__name__)
