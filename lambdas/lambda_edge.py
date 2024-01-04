###
### lambda@edge to redirect subdomains (intended for use with an origin request)
###
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    ## Capture the request header
    request = event["Records"][0]["cf"]["request"]
    ## The following lines are left here but commented out for any future debugging
    # logger.debug(event)

    ## Key fields/values
    origfqdn = request["headers"]["host"][0]["value"]
    logger.debug("Original FQDN = " + origfqdn)
    origbucket = request["origin"]["s3"]["domainName"]
    logger.debug("Original bucket = " + origbucket)
    ## The following lines are left here but commented out for any future debugging
    # origuri = request['uri']
    # logger.debug("Original URI ="+origuri)

    # split the FQDN into hostname + domainname
    orighost = origfqdn[: origfqdn.find(".", 0)]
    logger.info("Original Host = " + orighost)
    ## The following lines are left here but commented out for any future debugging
    # origdomain = origfqdn[origfqdn.find('.',0):]
    # logger.debug("Original Domain = "+origdomain)

    ## If the original hostname is cdn then don't do anything,
    if orighost == "cdn":
        request["headers"]["host"][0]["value"] = origbucket
        logger.debug("Request for CDN")
        logger.debug(request)
        return request

    ## otherwise rewrite the request to pull from the correct subfolder, log the rewrite request
    ## and reset the host value in the headers.
    else:
        request["origin"]["s3"]["path"] = "/" + orighost
        request["headers"]["host"][0]["value"] = origbucket
        logger.info("Rewrite request for vanity hostname")
        logger.debug(request)
        return request
