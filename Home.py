from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://smartbuzz.angelbroking.com/")

print("Current Page title: " + driver.title)

# slide the caraousel to left
driver.find_element_by_css_selector("body.body.modal-open:nth-child(2) div.new-republic-theme:nth-child(1) "
                                    "header.header.mobile-sticky-top.position-relative.z-999:nth-child(2) "
                                    "section.stocks-section.shadow-bottom.py-1.bg-white.py-0.border-top.border-bottom"
                                    ".bg-for-dark-version.px-1.px-sm-0 div.container-fluid.px-0 div.slider "
                                    "div.slider-company.owl-carousel.owl-theme.latest-smartmoney-slider.owl-loaded"
                                    ".owl-drag div.owl-nav button.owl-prev > svg:nth-child(1)").click()

# Slide the carousel to right
driver.find_element_by_css_selector("body.body.modal-open:nth-child(2) div.new-republic-theme:nth-child(1) "
                                    "header.header.mobile-sticky-top.position-relative.z-999:nth-child(2) "
                                    "section.stocks-section.shadow-bottom.py-1.bg-white.py-0.border-top.border-bottom"
                                    ".bg-for-dark-version.px-1.px-sm-0 div.container-fluid.px-0 div.slider "
                                    "div.slider-company.owl-carousel.owl-theme.latest-smartmoney-slider.owl-loaded"
                                    ".owl-drag div.owl-nav button.owl-next > svg:nth-child(1)").click()






# Read news page redirection
print("Current Page title: " + driver.title)
driver.find_element_by_css_selector("body.body.modal-open:nth-child(2) div.new-republic-theme:nth-child(1) "
                                    "header.header.mobile-sticky-top.position-relative.z-999:nth-child(2) "
                                    "div.container.pt-2 nav.navbar.navbar-expand-lg.navbar-light.p-0 "
                                    "div.collapse.navbar-collapse:nth-child(3) ul.navbar-nav.ml-auto "
                                    "li.nav-item.mx-xl-3:nth-child(1) > a.nav-link").click()
print("Current Page title after redirection: " + driver.title)
driver.back()
print("Current Page title after back: " + driver.title)

