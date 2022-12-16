首先我們前置作業為:
1.建立Lambda所需要的補丁包(layer)
	 $ pip install line-bot-sdk -t D:/temp
2.將temp內依照官方說法進行壓縮
	https://aws.amazon.com/tw/premiumsupport/knowledge-center/lambda-deployment-package-errors/
3.將壓縮包部屬到 AWS Lambda 下的 Layers
4.建立Lambda
5.貼上程式碼
6.在新建立的Lambda內將layer附加上
7.建立API Gatway
8.建立完的API Getway會有一組url，需附加進LINE開發者內此專案的webhook
9.測試
