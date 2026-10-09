def lambda_handler(event, context):
    print("CI/CD Sample Application - Version 2")

    return {
        "statusCode": 200,
        "body": "Hello! AWS CI/CD Pipeline Version 2 is working!"
    }