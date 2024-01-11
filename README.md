# cf-lambda-custom-domain

The Lamba@Edge function that handles path selection in the S3 origin for our custom domain CloudFront distribution.

## lambda_edge.py

See the Reference Material section for details on the origins of this code. This is a simple Python application to parse the `origin-request` payload in CloudFront and route the request to the correct subfolder based on the hostname in the domain of the request. There are currently no real tests to verify the functionality locally, but these will be coming soon.

## Development

- To preview a list of available Makefile commands: `make help`
- To install with dev dependencies: `make install`
- To update dependencies: `make update`
- To run unit tests: `make test`
- To lint the repo: `make lint`

## Required ENV

There is **NO** ENV since this code must run in Lambda@Edge which does not have ENV.

## Running locally

Other than the [tests/test_lambda_edge.py](./tests/test_lambda_edge.py), there are no other local run options at this time. More coming soon.

## Deployment

### Dev1 testing

The `make create-zip` command will package up the code into a `.zip` file, ready for upload to S3. The `make upload-zip` will upload the `.zip` package of the code to the `shared-files-<AWS_ACCT_NO>` bucket so that it is available for Terraform. The [mitlib-tf-workloads-libraries-website](https://github.com/MITLibraries/mitlib-tf-workloads-libraries-website) Terraform code is responsible for taking the `.zip` from S3, packaging it into a Lambda function, deploying a new version of the Lambda function, and then updating the CloudFront custom domain distribution to use the new version of the Lambda for the `origin-request` Lambda@Edge.

It is **NOT** possible to re-deploy the CloudFront distribution from the CLI (for now). Instead, there are GitHub Actions workflows in this repository that can be manually triggered from the GitHub web UI. One of those workflows will just redeploy CloudFront (it assumes that the developer has run `make upload-zip` first). This allows the developer to push an updated version of the application to Dev1 and test it in CloudFront without having to push work-in-progress code to GitHub.

It is also possible to run a more complete build-and-deploy workflow for Dev1 via the GitHub web UI: There is a second GitHub Actions workflow in this repository that can be manually trigger that will also run the `make create-zip` and `make upload-zip` with the version of code in GitHub and then redeploy CloudFront. This should be done before any PR is opened against the `main` branch.

### Automation

In line with our other CloudFront related workflows (see [web-images-static](https://github.com/MITLibraries/web-images-static)), there are automated workflows for merge to `main` and tagged releases on `main` that will automatically deploy this application to the Stage-Workloads and Prod-Workloads AWS Accounts, respectively.

## Reference Material

The following online resources were helpful in building the vanity hostname setup and Lambda@Edge function.

- [How to use Lambda@Edge with Terraform](https://advancedweb.hu/how-to-use-lambda-edge-with-terraform/)
- [How to use CloudFront Functions to Change the Origin Request Path](https://advancedweb.hu/how-to-use-cloudfront-functions-to-change-the-origin-request-path/)
- [AWS CloudFront Developer Guide: Lambda@Edge Examples](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html)
- [Multiple Websites with One S3 Bucket](https://opsdocks.com/posts/multiple-websites-one-s3/)
- [CloudFront with Mulitple Domains](https://moelholm.com/blog/2020/06/25/cloudfront-multiple-domains)
- [AWS CloudFront Developer Guide: Lambda Event Structure](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-event-structure.html#request-event-fields)
