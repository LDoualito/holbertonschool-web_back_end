#!/usr/bin/env python3
""" Client module test"""
import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """ Test the class """

    @parameterized.expand([
        ("google"),
        ('abc')
    ])
    @patch('client.get_json', return_value={})
    def test_org(self, org, patched):
        """ Test the org method """
        test = GithubOrgClient(org)
        self.assertEqual(test.org, patched.return_value)
        patched.assert_called_once()

    def test_public_repos_url(self):
        """ Test the public_repos_url method """
        expected = "https://api.github.com/orgs/google/repos"
        payload = {"repos_url": expected}
        patched = "client.GithubOrgClient.org"
        with patch(patched, PropertyMock(return_value=payload)):
            new = GithubOrgClient("google")
            self.assertEqual(new._public_repos_url, expected)

    @patch('client.get_json', return_value={})
    def test_public_repos(self, mocked):
        """ Test the public_repos method """
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock,
                   return_value=[]
                   ) as patched:
            new = GithubOrgClient("google")
            result = new.public_repos(license="f")
            self.assertEqual(result, patched.return_value)
            mocked.assert_called_once()
            patched.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """ Test the has_license method """
        test = GithubOrgClient('test')
        self.assertEqual(test.has_license(repo, license_key), expected)


@parameterized_class([{
    "org_payload": TEST_PAYLOAD[0][0],
    "repos_payload": TEST_PAYLOAD[0][1],
    "expected_repos": TEST_PAYLOAD[0][2],
    "apache2_repos": TEST_PAYLOAD[0][3]
}])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Test the integration """

    @classmethod
    def setUpClass(cls) -> None:
        """ SetUpClass """
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()
        mock_org = Mock()
        mock_org.json.return_value = cls.org_payload

        mock_repos = Mock()
        mock_repos.json.return_value = cls.repos_payload

        cls.mock_get.side_effect = [
            mock_org, mock_repos,
            mock_org, mock_repos
        ]

    @classmethod
    def tearDownClass(cls) -> None:
        """ tearDownClass """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """ Test the public_repos method """
        test = GithubOrgClient("google")
        response = test.public_repos()
        self.assertEqual(response, self.expected_repos)

    def test_public_repos_with_license(self):
        """ Test the public_repos method with license """
        test = GithubOrgClient("google")
        response = test.public_repos("apache-2.0")
        self.assertEqual(response, self.apache2_repos)
