import json
import unittest

import urllib
import urllib.error
import urllib.request


def get(url: str):
    try:
        with urllib.request.urlopen(url) as response:
            return {
                "content": response.read().decode("utf-8"),
                "status": response.status,
                "headers": response.getheaders(),
            }
    except urllib.error.HTTPError as e:
        return {"content": e.read().decode("utf-8"), "status": e.status}
    except urllib.error.URLError as e:
        print(f"Erorr: {e.reason}")


class TestService(unittest.TestCase):
    def setUp(self):
        self.backend_url = "http://nginx"

    def test_root(self):
        response = get(self.backend_url)

        self.assertEqual(response["content"], "Hello from Effective Mobile!")
        self.assertEqual(response["status"], 200)

    def test_other_routes(self):
        response = get(f"{self.backend_url}/other")

        self.assertEqual(response["content"], "Not Found")
        self.assertEqual(response["status"], 404)

    def test_healthy(self):
        response = get(f"{self.backend_url}/health")
        json_body = json.loads(response["content"])

        self.assertEqual(json_body["status"], "healthy")
        self.assertEqual(response["status"], 200)

    def test_server_tokens_off(self):
        response = get(self.backend_url)

        self.assertIn(("Server", "nginx"), response["headers"])


if __name__ == "__main__":
    unittest.main()
