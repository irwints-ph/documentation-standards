```bash
aws s3api create-bucket --bucket eds-eks-afk --region ap-southeast-1 --profile mys3 --create-bucket-configuration LocationConstraint=ap-southeast-1
https://eds-eks-afk.s3.amazonaws.com/index.html
aws s3 cp aws-files s3://eds-eks-afk/  --recursive --profile mys3

aws s3api put-public-access-block --bucket eds-eks-afk --public-access-block-configuration "BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=false,RestrictPublicBuckets=false"  --profile mys3

cd aws-files

aws s3api put-bucket-policy --bucket eds-eks-afk --policy "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Sid\":\"PublicReadGetObject\",\"Effect\":\"Allow\",\"Principal\":\"*\",\"Action\":\"s3:GetObject\",\"Resource\":\"arn:aws:s3:::eds-eks-afk/*\"}]}" --profile mys3

aws s3 website s3://eds-eks-afk/ --index-document index.html --error-document index.html  --profile mys3
aws s3api put-public-access-block --bucket eds-eks-afk --public-access-block-configuration "BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=false,RestrictPublicBuckets=false" --profile mys3
aws s3 website s3://eds-eks-afk/ --index-document index.html --error-document index.html --profile mys3
```


aws s3api put-bucket-policy --bucket eds-eks-afk --policy file://bucket-policy.json  --profile mys3

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::eds-eks-afk/*"
    }
  ]
}
```