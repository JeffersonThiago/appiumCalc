import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

class SimpleCalculatorTests(unittest.TestCase):

    @classmethod

    def setUpClass(self):
        #set up appium
        desired_caps = {}
        desired_caps["app"] = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            desired_capabilities= desired_caps)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def getresults(self):
        displaytext = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="CalculatorResults").text
        displaytext = displaytext.strip("Display is " )
        displaytext = displaytext.rstrip(' ')
        displaytext = displaytext.lstrip(' ')
        return displaytext


    def test_initialize(self):
        self.driver.find_element(by=AppiumBy.NAME, value ="Limpar").click()
        self.driver.find_element(by=AppiumBy.NAME, value ="Sete").click()
        self.assertEqual(self.getresults(),"Exibição é 7")
        self.driver.find_element(by=AppiumBy.NAME, value ="Limpar").click()

    def test_addition(self):
        self.driver.find_element(by=AppiumBy.NAME, value ="Um").click()
        self.driver.find_element(by=AppiumBy.NAME, value ="Mais").click()
        self.driver.find_element(by=AppiumBy.NAME, value ="Sete").click()
        self.driver.find_element(by=AppiumBy.NAME, value ="Igual a").click()
        self.assertEqual(self.getresults(),"Exibição é 8")
        self.driver.find_element(by=AppiumBy.NAME, value ="Limpar").click()

    def test_combination(self):
        self.driver.find_element(by=AppiumBy.NAME, value ="Sete").click()
        self.driver.find_element(by=AppiumBy.NAME, value ="Multiplicar por").click()
        self.driver.find_element(by=AppiumBy.NAME, value ="Nove").click()
        self.driver.find_element(by=AppiumBy.NAME, value ="Mais").click()
        self.driver.find_element(by=AppiumBy.NAME, value ="Um").click()
        self.driver.find_element(by=AppiumBy.NAME, value ="Igual a").click()
        self.driver.find_element(by=AppiumBy.NAME, value ="Dividir por").click()
        self.driver.find_element(by=AppiumBy.NAME, value ="Oito").click()
        self.driver.find_element(by=AppiumBy.NAME, value ="Igual a").click()
        self.assertEqual(self.getresults(),"Exibição é 8")
        self.driver.find_element(by=AppiumBy.NAME, value ="Limpar").click()

    def test_division(self):
        self.driver.find_element(by=AppiumBy.NAME, value ="Oito").click()
        self.driver.find_element(by=AppiumBy.NAME, value ="Oito").click()
        self.driver.find_element(by=AppiumBy.NAME, value ="Dividir por").click()
        self.driver.find_element(by=AppiumBy.NAME, value ="Um").click()
        self.driver.find_element(by=AppiumBy.NAME, value ="Um").click()
        self.driver.find_element(by=AppiumBy.NAME, value ="Igual a").click()
        self.assertEqual(self.getresults(),"Exibição é 8")
        self.driver.find_element(by=AppiumBy.NAME, value ="Limpar").click()

    def test_multiplication(self):
        self.driver.find_element(by=AppiumBy.NAME, value ="Nove").click()
        self.driver.find_element(by=AppiumBy.NAME, value ="Multiplicar por").click()
        self.driver.find_element(by=AppiumBy.NAME, value ="Nove").click()
        self.driver.find_element(by=AppiumBy.NAME, value ="Igual a").click()
        self.assertEqual(self.getresults(),"Exibição é 81") 
        self.driver.find_element(by=AppiumBy.NAME, value ="Limpar").click()

    def test_subtraction(self):
        self.driver.find_element(by=AppiumBy.NAME, value ="Nove").click()
        self.driver.find_element(by=AppiumBy.NAME, value ="Menos").click()
        self.driver.find_element(by=AppiumBy.NAME, value ="Um").click()
        self.driver.find_element(by=AppiumBy.NAME, value ="Igual a").click()
        self.assertEqual(self.getresults(),"Exibição é 8")
        self.driver.find_element(by=AppiumBy.NAME, value ="Limpar").click()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleCalculatorTests)
    unittest.TextTestRunner(verbosity=2).run(suite)