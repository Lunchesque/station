 def creating_users(self, data):
        driver = self.app.driver
        self.app.session.being_on_users_page()
        addBtn = driver.find_element_by_xpath("//button[contains(@ng-click, 'create()')]")
        ActionChains(driver).move_to_element(addBtn).click(addBtn).perform()
        Select(driver.find_element_by_name("role")).select_by_index(data.role)
        if data.role == 3:
            path = "/home/sergey/Selenium/Project/files/admin_avatar.jpg"
        elif data.role == 2:
            path = "/home/sergey/Selenium/Project/files/oper_avatar.jpg"
        elif data.role == 1:
            path = "/home/sergey/Selenium/Project/files/watcher_avatar.jpg"
        elif data.role == 0:
            path = "/home/sergey/Selenium/Project/files/guest_avatar.png"
        imgUploadEl = driver.find_element_by_xpath("//input[@name='avatar']")
        imgUploadEl.send_keys(path)

        userRole = driver.find_element_by_name("role").get_attribute("value")

        driver.find_element_by_name("email").send_keys(data.email.format(userRole, data.userId))
        driver.find_element_by_name("phone").send_keys(data.phone)
        driver.find_element_by_name("fullName").send_keys(data.name.format(userRole, data.userId))

        driver.find_element_by_name("autoGeneratePassword").click()
        driver.find_element_by_name("showPasswords").click()
        driver.find_element_by_name("password").send_keys(data.name.format(userRole, data.userId))
        driver.find_element_by_name("password_confirmation").send_keys(data.name.format(userRole, data.userId))
        if data.role == 3:
            driver.find_element_by_name("enableNotifications").click()
        driver.find_element_by_xpath("//button[@ng-click='save()']").click()
        ActionChains(driver).pause(0.1).perform()
        self.users_cache = None
