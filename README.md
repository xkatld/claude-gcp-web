# claude-gcp-web
web端使用gcp的claude3.5
# 安装python3
环境：Ubuntu24
```shell
apt update -y
apt install python3 python3-pip -y
```
```shell
rm /usr/lib/python3.12/EXTERNALLY-MANAGED
pip3 install flask anthropic[vertex] python-dotenv
```
# 安装gcloud CLI
```shell
apt update -y
apt install apt-transport-https ca-certificates gnupg curl sudo -y
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg
echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
```
```shell
apt update -y
apt install google-cloud-cli -y
```
# 配置gcloud CLI
登录到您的 Google Cloud 账户：
```shell
gcloud auth login
```
设置正确的项目：
确保您使用的是正确的 Google Cloud 项目。运行：
```shell
gcloud config set project <项目ID>
```
按照提示在浏览器中完成登录。
设置应用默认凭证（Application Default Credentials，ADC）：
```shell
gcloud auth application-default login
```
这会在您的本地机器上设置默认凭证。
# git 代码
```shell
apt update -y
apt install git -y
git clone https://github.com/xkatld/claude-gcp-web.git claudeweb
cd claudeweb
```
请修改'app.py'，'.env'文件
启动即可，默认端口为：14514
```shell
python3 app.py
```
