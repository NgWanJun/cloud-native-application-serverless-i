import boto3
import random
import json

s3 = boto3.resource('s3')
bucket_name = 'somecuteanimals1'

def picture(event, context):
    bucket = s3.Bucket(bucket_name)
    objects = list(bucket.objects.all())

    # Pick random object
    random_object = random.choice(objects)

    # Generate a pre-signed URL for the object
    url = s3.meta.client.generate_presigned_url(
        'get_object',
        Params={'Bucket': bucket_name, 'Key': random_object.key},
        ExpiresIn=3600
    )

    # Return a JSON response with the URL and some text
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps({'url': url, 'text': 'Yay a cute animal!'})
    }   