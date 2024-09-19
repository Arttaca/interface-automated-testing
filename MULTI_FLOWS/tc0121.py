from seleniumbase import SB
import seleniumbase
import time
import os

def test_01_21(url):
    with SB(
        extension_dir=os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'temp', 'metamask-chrome'))
        ) as sb:
        url = "https://development.arttaca.io/nft/hehehehehehe/2"
        sb.sleep(5)
        sb.switch_to_window(1)
        sb.click('input[data-testid="onboarding-terms-checkbox"]')
        sb.click('button:contains("Import an existing wallet")')
        sb.click('#metametrics-opt-in')
        sb.click('button:contains("I agree")')
        sb.type('input[data-testid="import-srp__srp-word-0"]',"dune")
        sb.type('input[data-testid="import-srp__srp-word-1"]',"song")
        sb.type('input[data-testid="import-srp__srp-word-2"]',"course")
        sb.type('input[data-testid="import-srp__srp-word-3"]',"tumble")
        sb.type('input[data-testid="import-srp__srp-word-4"]',"small")
        sb.type('input[data-testid="import-srp__srp-word-5"]',"coast")
        sb.type('input[data-testid="import-srp__srp-word-6"]',"pudding")
        sb.type('input[data-testid="import-srp__srp-word-7"]',"little")
        sb.type('input[data-testid="import-srp__srp-word-8"]',"leaf")
        sb.type('input[data-testid="import-srp__srp-word-9"]',"churn")
        sb.type('input[data-testid="import-srp__srp-word-10"]',"umbrella")
        sb.type('input[data-testid="import-srp__srp-word-11"]',"junior")
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
        sb.click('div.ActionButtons__ButtonBox-sc-1bj8kp4-1.dZzVJr')
        print(sb.is_text_visible("Burn"))
        sb.sleep(30)

if __name__ == "__main__":
    test_01_21("https://development.arttaca.io/nft/hehehehehehe/2")