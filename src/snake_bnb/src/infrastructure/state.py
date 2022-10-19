from typing import Optional

from data.owners import Owner
import services.data_service as service

active_account: Optional[Owner] = None


def reload_account():
    global active_account
    if not active_account:
        return

    active_account = service.find_account_by_email(active_account.email)
