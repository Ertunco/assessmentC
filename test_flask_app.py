try:
    import unittest
    import flask_app as fl_app
    from flask_app import app
    import pandas as pd
    from selenium import webdriver
except Exception as e:
    print(f"Some modules are missing {e}")

class TestFlaskApp(unittest.TestCase):
    # Check for response
    def test_response(self):
        tester = app.test_client()
        response = tester.get("/")
        self.assertEqual(response.status_code, 200)
        response = tester.get("/login")
        self.assertEqual(response.status_code, 200)
        response = tester.get("/symbol")
        self.assertEqual(response.status_code, 200)
        response = tester.get("/function")
        self.assertEqual(response.status_code, 404)
        response = tester.get("/nonexistingroute")
        self.assertEqual(response.status_code, 404)

    # Check login page content
    def test_login_page_loads(self):
        tester = app.test_client()
        response = tester.get("/login")
        self.assertTrue(b'Enter your API key' in response.data)
        response = tester.get("/login")
        self.assertTrue(b'API Key: ' in response.data)
        response = tester.get("/login")
        self.assertTrue(b'Login' in response.data)
        response = tester.get("/login")
        self.assertFalse(b'Login Here: ' in response.data)
        response = tester.get("/login")
        self.assertFalse(b'Someting that doesnt exist in Login Page' in response.data)

    def test_check_file_name(self):
        self.assertFalse(fl_app.generate_list_dict_from_df("somefilename.csv"))
        self.assertFalse(fl_app.generate_list_dict_from_df("nsdq.csv"))
        self.assertIsInstance(fl_app.generate_list_dict_from_df("nasdaq.csv"), list)

    def test_check_Df_cols(self):
        df_test = pd.DataFrame(columns=['A','B','C','D','E','F','G'])
        self.assertFalse(fl_app.check_df_cols(df_test))
 

if __name__ == "__main__":
    unittest.main()