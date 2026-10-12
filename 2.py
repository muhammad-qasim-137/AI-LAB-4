class PasswordVault:
    def __init__(self, username, password):
        self.username = username
        self._vault_status = "Locked"
        self.__password = password

    def change_password(self, old_password, new_password):
        if self.__password == old_password:
            self.__password = new_password
            print("Password changed")
        else:
            print("Incorrect password")

    def verify_password(self, entered_password):
        if entered_password == self.__password:
            self._vault_status = "Unlocked"
            print("Access Granted")
        else:
            print("Access Denied")

    def display_status(self):
        print("Vault status:", self._vault_status)


vault = PasswordVault("user1", "pass123")
vault.verify_password("pass123")
vault.display_status()
vault.change_password("pass123", "newpass456")
vault.verify_password("newpass456")
