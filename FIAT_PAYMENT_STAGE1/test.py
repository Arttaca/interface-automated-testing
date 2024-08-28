from seleniumbase import SB
import seleniumbase
import time
import os
def test_swag_labs():
    with SB() as self:
        self.open("https://development.arttaca.io/")
        self.click('button:contains("Connect")')
        self.click('button:contains("Connect a wallet")')
        self.click('button:contains("MetaMask")')
        time.sleep(5)
def test_metamask():
    with SB(
        demo=True,
        extension_dir=os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'temp', 'metamask-chrome'))
        ) as sb:
        sb.sleep(3)
        sb.switch_to_newest_window()
        print(sb.get_current_url())
        sb.click('#onboarding__terms-checkbox')

if __name__ == "__main__":
    test_metamask()