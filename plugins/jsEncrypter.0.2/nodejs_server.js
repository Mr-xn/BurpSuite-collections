/**
 * author: c0ny1
 * date: 2018-4-14
 * file: nodejs_server.js
 */
var http = require('http');
var querystring = require('querystring');
var host = '127.0.0.1'; //地址
var port = '1664'; //端口
//require('your_encrypte_script.js'); /*引入实现加密的js文件*/
require('./sha384.js');
// 处理函数
function js_encrypt(payload){
	var newpayload;
	/**********在这里编写调用加密函数进行加密的代码************/

	/**********************************************************/
	return newpayload;
}
var server = http.createServer(function(request,response){
	if(request.method === 'POST'){
		var postData = '';
		request.on('data',function(params){
			postData += params;
		});
		
		request.on('end',function(){
			var dataString = postData.toString();
			var dataObj = querystring.parse(dataString);
			var payload = dataObj.payload;
			var encrypt_payload = js_encrypt(payload); 
			console.log('[+] ' + payload + ':' + encrypt_payload);
			
			response.statusCode = 200;
			response.write(encrypt_payload);
			response.end();
		});
	}else{
		response.statusCode = 200;
		response.write("^_^\n\rhello jsEncrypter!");
		response.end();
	}
});
server.listen(port, host, function () {
	console.log("[!] ^_^");
	console.log("[*] nodejs server start!");
	console.log("[+] address: http://"+host+":"+port);
});