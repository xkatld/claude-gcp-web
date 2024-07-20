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
c
# 配置gcloud CLI
登录到您的 Google Cloud 账户：
```shell
gcloud auth login
```
按照提示在浏览器中完成登录。
设置应用默认凭证（Application Default Credentials，ADC）：
```shell
cloud auth application-default login
```
这会在您的本地机器上设置默认凭证。
设置正确的项目：
确保您使用的是正确的 Google Cloud 项目。运行：
```shell
gcloud config set project <项目ID>
```


