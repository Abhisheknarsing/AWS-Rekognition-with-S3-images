import boto3


S3_BASE_URL = 'Your Url'
# eg.. https://s3-us-west-2.amazonaws.com/
BUCKET = 'Your Bucket Name'
AWS_ACCESS_KEY_ID = 'Your Access Key ID'
AWS_SECRET_ACCESS_KEY = 'Access Secret Key'

#images in your bucket name
First_image = "obama.png"
Second_image = "obama2.png"


s3 = boto3.resource('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                    region_name='us-west-2')
bucket = s3.Bucket(BUCKET)

rekognition = boto3.client('rekognition', aws_access_key_id=AWS_ACCESS_KEY_ID,
                           aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name='us-west-2')


FaceMatch = False

try:
    response = rekognition.compare_faces(
        SourceImage={
            'S3Object': {
                'Bucket': BUCKET,
                'Name': First_image
            }
        },
        TargetImage={
            'S3Object': {
                'Bucket': BUCKET,
                'Name': Second_image
            }
        },
        QualityFilter='HIGH'
    )


    for key, value in response.items():
        if key in ('FaceMatches'):
           if len(value) != 0:
            if value[0]['Similarity'] > 70:
                FaceMatch = True

    print(FaceMatch)
except rekognition.exceptions.InvalidParameterException as e:
    print("no face")
