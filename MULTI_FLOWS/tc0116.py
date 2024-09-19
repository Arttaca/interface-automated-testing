from seleniumbase import SB
import seleniumbase
import time
import os

def test_01_16():
    with SB(
        extension_dir=os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'temp', 'metamask-chrome'))
        ) as sb:
        url = "https://development.arttaca.io/nft/test-multi2/5"
        sb.sleep(5)
        sb.switch_to_window(1)
        sb.click('input[data-testid="onboarding-terms-checkbox"]')
        sb.click('button:contains("Import an existing wallet")')
        sb.click('#metametrics-opt-in')
        sb.click('button:contains("I agree")')
        sb.type('input[data-testid="import-srp__srp-word-0"]',"noodle")
        sb.type('input[data-testid="import-srp__srp-word-1"]',"shy")
        sb.type('input[data-testid="import-srp__srp-word-2"]',"west")
        sb.type('input[data-testid="import-srp__srp-word-3"]',"loyal")
        sb.type('input[data-testid="import-srp__srp-word-4"]',"stone")
        sb.type('input[data-testid="import-srp__srp-word-5"]',"present")
        sb.type('input[data-testid="import-srp__srp-word-6"]',"asthma")
        sb.type('input[data-testid="import-srp__srp-word-7"]',"target")
        sb.type('input[data-testid="import-srp__srp-word-8"]',"space")
        sb.type('input[data-testid="import-srp__srp-word-9"]',"tattoo")
        sb.type('input[data-testid="import-srp__srp-word-10"]',"disorder")
        sb.type('input[data-testid="import-srp__srp-word-11"]',"desk")
        sb.click('button:contains("Confirm Secret Recovery Phrase")')
        password = "Hieu12344."
        sb.type('input[data-testid="create-password-new"]',password)
        sb.type('input[data-testid="create-password-confirm"]',password)
        sb.click('input[data-testid="create-password-terms"]')
        sb.click('button:contains("Import my wallet")')
        sb.click('button:contains("Got it")')
        sb.click('button:contains("Next")')
        sb.click('button:contains("Done")')
        sb.sleep(5)
        sb.click('button[data-testid="network-display"]')
        sb.click('input[type="checkbox"]')
        sb.click('p:contains("Sepolia")')
        sb.open_new_window()
        sb.open(url)
        sb.click('button:contains("Connect")')
        sb.click('span:contains("Connect a Wallet")')
        sb.click('button:contains("MetaMask")')
        sb.sleep(15)
        sb.switch_to_window(4)
        sb.click('button:contains("Next")')
        sb.click('button:contains("Confirm")')
        sb.sleep(7)
        sb.switch_to_window(3)
        sb.click('button.css-hnz0pg')
        sb.sleep(7)
        sb.switch_to_window(4)
        sb.click('button:contains("Confirm")')
        sb.sleep(7)
        sb.switch_to_window(3)
        sb.click(".three-dots")
        sb.click('button:contains("Burn")')
        sb.type("#quantity", "1")
        sb.click('button:contains("Confirm")')
        sb.sleep(17)
        sb.switch_to_window(4)
        sb.click('button:contains("Reject")') #Confirm
        sb.sleep(30)
        
if __name__ == "__main__":
    test_01_16("https://development.arttaca.io/nft/test-multi2/5")