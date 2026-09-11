"""Streamlit Community Cloud keep-alive visitor.

curl 등 단순 HTTP 요청은 Streamlit이 반환하는 정적 HTML 셸만 받을 뿐, 실제
Python 앱(WebSocket 세션)을 띄우지 않아 슬립 방지 효과가 없다. 헤드리스
브라우저로 페이지를 실제로 렌더링해 방문해야 "진짜 방문"으로 집계된다.
"""

from playwright.sync_api import sync_playwright

URL = "https://payment-conversion-prediction-kfmzlsbdapywsfresbxfkm.streamlit.app/"


def main() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(URL, wait_until="domcontentloaded", timeout=120_000)
        page.wait_for_timeout(5_000)

        wake_button = page.get_by_role("button", name="Yes, get this app back up!")
        if wake_button.count() > 0:
            print("App is asleep — clicking wake-up button")
            wake_button.click()
            page.wait_for_timeout(60_000)
        else:
            print("App already awake")

        print(f"Final page title: {page.title()!r}")
        browser.close()


if __name__ == "__main__":
    main()
