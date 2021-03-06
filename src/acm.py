import boto3
from src.environment import Environment


class ACM():
    """ Class to interact with AWS ACM to manage certificates. """
    def __init__(self):
        """ Class constructor. """
        self.client = boto3.client(
            'acm',
            aws_access_key_id = Environment.aws_access_key,
            aws_secret_access_key = Environment.aws_secret_key,
            region_name = Environment.aws_region
        )


    def list_certificates(self):
        """ Lists all certificates in ACM. """
        return self.client.list_certificates(
            MaxItems = 123
        )


    def get_certificate(self, certificate_arn):
        """
        Lists certificate information by certificate ARN.

        :param certificate_arn: unique certificate_arn provided by amazon
        """
        return self.client.get_certificate(
            CertificateArn = certificate_arn
        )
