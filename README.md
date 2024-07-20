# claude-gcp-web
web端使用gcp的claude3.5
# 安装python3
环境：Ubuntu24
```shell
apt update -y
apt install python3 python3-pip -y
```
```shell
pip3 install flask anthropic[vertex] python-dotenv
```
# 安装gcloud CLI
```shell
apt update -y
apt install apt-transport-https ca-certificates gnupg curl sudo -y
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg
echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
apt install google-cloud-cli -y
```
# 配置gcloud CLI
```shell
gcloud init
```
