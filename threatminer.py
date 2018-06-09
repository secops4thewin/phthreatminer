# Threat Miner Class
import requests
import logging
import json
import datetime
import re
import time

# Establish Logging.
logging.basicConfig()
logger = logging.getLogger('ThreatMiner')

class threatMiner():
    def __init__(
        self,
        # Replace the base url to the url that you need
        base_url='https://api.threatminer.org/v2/',
        prettyPrint=False
    ):
        """
        Threat Miner Python Wrapper.

        Available Functions
        - test_connect              Provides a method to test connectivity
        - first_function            This is example text that you can replace to describe a function
        
        Usage:
        # Should match your class name.  Delete this line
        s = threatMiner()

        s.function_name(valid_variables)
        """

        # Create Requests Session
        self.session = requests.session()
        # Create Base URL variable to allow for updates in the future
        self.base_url = base_url
        # Create Pretty Print variable
        self.prettyPrint = prettyPrint

        # Create endpoint
        endpoint = '{}domain.php?q=vwrm.com&rt=1'.format(self.base_url)

        # Initiate Ping to Threat Miner Endpoint
        self.ping = self.session.get(endpoint)

        # Request failed returning false and logging an error
        if self.ping.status_code != 200:
            logger.error(
                "Error connecting to Threat Miner, error message: {}".format(
                    self.ping.text))

    def parse_output(self, input):
        # If prettyPrint set to False
        if self.prettyPrint is False:
            return json.dumps(input)
        # If prettyPrint set to True
        elif self.prettyPrint is True:
            print json.dumps(input, indent=4)
    
    #Delete this comment line after amending below line -  Update this line to reflect the true endpoint
    def test_connect(self):
        """
        Function:   Test ping to Threat Miner API

        Usage:
        s = threatMiner()
        s.test_connect()
        """

        endpoint = '{}ping'.format(self.base_url)
        # Make connection to the ping endpoint
        r = self.session.get(endpoint)
        # Specify Output as JSON
        output = r.json()
        # If the request is successful
        if r.status_code == 200:
            return True
        # Request failed returning false and logging an error
        else:
            logger.warning(
                "test_connect:Error with query to threatMiner, error message: {}".format(
                    output['message']))
            return False
    def get_domain(self, domain, function):
        """
        Function:   This function performs lookups against domains depending on the function
        
        :param function: Required - These are the functions that threat miner provide for domain lookups
        Functions
            1 - WHOIS
            2 - Passive DNS
            3 - Example Query URI
            4 - Related Samples (hash only)
            5 - Subdomains
            6 - Report tagging

        Usage:
        s = threatMiner()
        s.get_domain("vwrm.com", 1)
        """
        # URL that we are querying
        endpoint = '{}/domain.php?q={}&rt={}'.format(self.base_url, domain, function)
        # Create a request
        r = self.session.get(endpoint)
        # Sleep to ensure throttling
        time.sleep(7)
        # If the request is successful
        if r.status_code == 200:
            output = r.json()
            return self.parse_output(output)
        # Request failed returning false and logging an error
        else:
            # Write a warning to the console
            logger.warning(
                "get_domain:Error with query to threatMiner, error message: {}".format(
                     r.json()['status_message']))
            return False

    def get_ip(self, ip, function):
        """
        Function:   This function performs lookups against IPs depending on the function

        :param function: Required - These are the functions that threat miner provide for ip lookups

        Flags
            1 - WHOIS
            2 - Passive DNS
            3 - URIs
            4 - Related Samples (hash only)
            5 - SSL Certificates (hash only)
            6 - Report tagging

        Usage:
        s = threatMiner()
        s.get_ip("216.58.213.110", 1)
        """
        # URL that we are querying
        endpoint = '{}/host.php?q={}&rt={}'.format(self.base_url, ip, function)
        # Create a request
        r = self.session.get(endpoint)
        # Sleep to ensure throttling
        time.sleep(7)
        # If the request is successful
        if r.status_code == 200:
            output = r.json()
            return self.parse_output(output)
        # Request failed returning false and logging an error
        else:
            # Write a warning to the console
            logger.warning(
                "get_ip:Error with query to threatMiner, error message: {}".format(
                     r.json()['status_message']))
            return False

    def get_sample(self, sample, function):
        """
        Function:   This function performs lookups against hashes depending on the functions

        :param function: Required - These are the functions that threat miner provide for hash lookups

        Flags
            1 - Metadata
            2 - HTTP Traffic
            3 - Hosts (domains and IPs)
            4 - Mutants
            5 - Registry Keys
            6 - AV Detections
            7 - Report tagging

        Usage:
        s = threatMiner()
        s.get_sample("abe4a942cb26cd87a35480751c0e50ae", 1)
        """
        # URL that we are querying
        endpoint = '{}/sample.php?q={}&rt={}'.format(self.base_url, sample, function)
        # Create a request
        r = self.session.get(endpoint)
        # Sleep to ensure throttling
        time.sleep(7)
        # If the request is successful
        if r.status_code == 200:
            output = r.json()
            return self.parse_output(output)
        # Request failed returning false and logging an error
        else:
            # Write a warning to the console
            logger.warning(
                "get_sample:Error with query to threatMiner, error message: {}".format(
                     r.json()['status_message']))
            return False

    def get_imphash(self, imphash, function):
        """
        Function:   This function performs lookups against imphashes depending on the functions

        :param function: Required - These are the functions that threat miner provide for imphashes lookups

        Flags
            1 - Metadata
            2 - HTTP Traffic
            3 - Hosts (domains and IPs)
            4 - Mutants
            5 - Registry Keys
            6 - AV Detections
            7 - Report tagging

        Usage:
        s = threatMiner()
        s.get_sample("abe4a942cb26cd87a35480751c0e50ae", 1)
        """
        # URL that we are querying
        endpoint = '{}/imphash.php?q={}&rt={}'.format(self.base_url, imphash, function)
        # Create a request
        r = self.session.get(endpoint)
        # Sleep to ensure throttling
        time.sleep(7)
        # If the request is successful
        if r.status_code == 200:
            output = r.json()
            return self.parse_output(output)
        # Request failed returning false and logging an error
        else:
            # Write a warning to the console
            logger.warning(
                "get_imphash:Error with query to threatMiner, error message: {}".format(
                     r.json()['status_message']))
            return False

    def get_ssdeep(self, ssdeep, function):
        """
        Function:   This function performs lookups against ssdeep depending on the functions

        :param function: Required - These are the functions that threat miner provide for ssdeep lookups

        Flags
            1 - Samples
            2 - Report tagging

        Usage:
        s = threatMiner()
        s.get_ssdeep("1536:TJsNrChuG2K6IVOTjWko8a9P6W3OEHBQc4w4:TJs0oG2KSTj3o8a9PFeEHn4l", 1)
        """
        # URL that we are querying
        endpoint = '{}/ssdeep.php?q={}&rt={}'.format(self.base_url, ssdeep, function)
        # Create a request
        r = self.session.get(endpoint)
        # Sleep to ensure throttling
        time.sleep(7)
        # If the request is successful
        if r.status_code == 200:
            output = r.json()
            return self.parse_output(output)
        # Request failed returning false and logging an error
        else:
            # Write a warning to the console
            logger.warning(
                "get_ssdeep:Error with query to threatMiner, error message: {}".format(
                     r.json()['status_message']))
            return False

    def get_ssl(self, ssl, function):
        """
        Function:   This function performs lookups against ssl depending on the functions

        :param function: Required - These are the functions that threat miner provide for ssl lookups

        Flags
            1 - Hosts
            2 - Report tagging

        Usage:
        s = threatMiner()
        s.get_ssl("42a8d5b3a867a59a79f44ffadd61460780fe58f2", 1)
        """
        # URL that we are querying
        endpoint = '{}/ssl.php?q={}&rt={}'.format(self.base_url, ssl, function)
        # Create a request
        r = self.session.get(endpoint)
        # Sleep to ensure throttling
        time.sleep(7)
        # If the request is successful
        if r.status_code == 200:
            output = r.json()
            return self.parse_output(output)
        # Request failed returning false and logging an error
        else:
            # Write a warning to the console
            logger.warning(
                "get_ssl:Error with query to threatMiner, error message: {}".format(
                     r.json()['status_message']))
            return False

    def get_email(self, email, function):
        """
        Function:   This function performs lookups against email depending on the functions

        :param function: Required - These are the functions that threat miner provide for email lookups
        Flags
            1 - Domains

        Usage:
        s = threatMiner()
        s.get_email("42a8d5b3a867a59a79f44ffadd61460780fe58f2", 1)
        """
        # URL that we are querying
        endpoint = '{}/email.php?q={}&rt={}'.format(self.base_url, email, function)
        # Create a request
        r = self.session.get(endpoint)
        # Sleep to ensure throttling
        time.sleep(7)
        # If the request is successful
        if r.status_code == 200:
            output = r.json()
            return self.parse_output(output)
        # Request failed returning false and logging an error
        else:
            # Write a warning to the console
            logger.warning(
                "get_email:Error with query to threatMiner, error message: {}".format(
                     r.json()['status_message']))
            return False
 
    def get_av(self, av, function):
        """
        Function:   This function performs lookups against AV depending on the functions

        :param function: Required - These are the functions that threat miner provide for AV lookups
        Flags
            1 - Samples
            2 - Report tagging

        Usage:
        s = threatMiner()
        s.get_av("Trojan.Enfal", 1)
        """
        # URL that we are querying
        endpoint = '{}/email.php?q={}&rt={}'.format(self.base_url, av, function)
        # Create a request
        r = self.session.get(endpoint)
        # Sleep to ensure throttling
        time.sleep(7)
        # If the request is successful
        if r.status_code == 200:
            output = r.json()
            return self.parse_output(output)
        # Request failed returning false and logging an error
        else:
            # Write a warning to the console
            logger.warning(
                "get_av:Error with query to threatMiner, error message: {}".format(
                     r.json()['status_message']))
            return False

 