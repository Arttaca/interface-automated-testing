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
        extension_dir=os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'temp', 'metamask-chrome'))
        ) as sb:
        sb.sleep(5)
        sb.switch_to_window(1)
        sb.click('input[data-testid="onboarding-terms-checkbox"]')
        sb.click('button:contains("Import an existing wallet")')
        sb.click('#metametrics-opt-in')
        sb.click('button:contains("I agree")')
        sb.type('input[data-testid="import-srp__srp-word-0"]',"caution")
        sb.type('input[data-testid="import-srp__srp-word-1"]',"flee")
        sb.type('input[data-testid="import-srp__srp-word-2"]',"oil")
        sb.type('input[data-testid="import-srp__srp-word-3"]',"melody")
        sb.type('input[data-testid="import-srp__srp-word-4"]',"carry")
        sb.type('input[data-testid="import-srp__srp-word-5"]',"inform")
        sb.type('input[data-testid="import-srp__srp-word-6"]',"pizza")
        sb.type('input[data-testid="import-srp__srp-word-7"]',"enemy")
        sb.type('input[data-testid="import-srp__srp-word-8"]',"vacuum")
        sb.type('input[data-testid="import-srp__srp-word-9"]',"success")
        sb.type('input[data-testid="import-srp__srp-word-10"]',"like")
        sb.type('input[data-testid="import-srp__srp-word-11"]',"aisle")
        sb.click('button:contains("Confirm Secret Recovery Phrase")')
        password = "Hieu12344."
        sb.type('input[data-testid="create-password-new"]',password)
        sb.type('input[data-testid="create-password-confirm"]',password)
        sb.click('input[data-testid="create-password-terms"]')
        sb.click('button:contains("Import my wallet")')
        sb.click('button:contains("Got it")')
        sb.click('button:contains("Next")')
        sb.click('button:contains("Done")')
        sb.open_new_window()
        sb.open("https://development.arttaca.io/")
        sb.click('button:contains("Connect")')
        sb.click('button:contains("Connect a wallet")')
        sb.click('button:contains("MetaMask")')
        sb.sleep(7)
        sb.switch_to_window(4)
        sb.click('button:contains("Next")')
        sb.click('button:contains("Confirm")')
        sb.switch_to_window(2)
        # print(sb.get_current_url())
        sb.switch_to_window(3)
        # print(sb.get_current_url())
        sb.click('button.css-zjr4b9')
        sb.sleep(7)
        sb.switch_to_window(4)
        print(sb.get_current_url())
        sb.click('button:contains("Confirm")')
        sb.sleep(20)


if __name__ == "__main__":
    test_metamask()