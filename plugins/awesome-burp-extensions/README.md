# Awesome Burp Extensions  [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
A curated list of amazingly awesome Burp Extensions

## 国外师傅收集的精选`burp`插件列表：[awesome-burp-extensions](https://github.com/snoopysecurity/awesome-burp-extensions)  
> 我慢慢同步翻译成中文版本 -_-  

# Contributing-贡献

[Please refer to the contributing guide for details](https://github.com/snoopysecurity/awesome-burp-extensions/blob/master/CONTRIBUTING.md).  
> 如果想贡献好的插件，请按照项目里的贡献模板来提交

# How to Use-怎样使用
Awesome burp extensions is an amazing list for people who want to spice up their Burp instance with awesome plugins. The best ways to use are:
 - Simply press command + F to search for a keyword
 - Go through our Content Menu.
> 一句话，快速搜索:`Windows:CTRL+F`/`Mac:Command+F`搜索，要不就慢慢浏览我们的菜单吧-_-||

# Content-内容目录
- [Scanners](#scanners)-扫描类
- [Custom Features](#custom-features)-自定义功能类
- [Beautifiers and Decoders](#beautifiers-and-decoders)-美化和解码相关
- [Cloud Security](#cloud-security)-云安全,主要是AWS这类`真云`
- [Scripting](#scripting)-脚本相关
- [OAuth and SSO](#oauth-and-sso)-开放授权(OAuth)和单点登录(SSO)相关安全检测插件
- [Information Gathering](#information-gathering)-信息收集
- [Vulnerability Specific Extensions](#vulnerability-specific-extensions)-各个类型漏洞相关插件
    - [Cross-site scripting](#cross-site-scripting)-跨站脚本
    - [SSRF](#server-side-request-forgery)-SSRF(服务器端请求伪造)
    - [Broken Access Control](#broken-access-control)-越权访问（Broken Access Control，简称BAC）
    - [Cross-Site Request Forgery](#cross-site-request-forgery)-跨站请求伪造,注意和SSRF区别
    - [Deserialization](#deserialization)-反序列化,一般用于检查Java/PHP这类常见动态语言
    - [Sensitive Data Exposure](#sensitive-data-exposure)-敏感信息泄露
    - [SQL Injection](#sql-injection)-熟悉的`SQL`注入
    - [XXE](#xxe)-XXE(XML External Entity,也就是XML外部实体注入攻击)[详细介绍一](https://www.freebuf.com/articles/web/126788.html) | [详细介绍二](https://xz.aliyun.com/t/3357)
    - [Insecure File Uploads](#insecure-file-uploads)-不安全的文件上传
    - [Directory Traversal](#directory-traversal)-列目录，目录遍历
    - [Session Management](#session-management)-会话管理，越权检测、随机请求头、WAF探测
    - [Command Injection](#command-injection)-命令注入
- [Web Application Firewall Evasion](#web-application-firewall-evasion)-bypass WAF相关插件
- [Logging and Notes](#logging-and-notes)-日志和备注相关
- [Payload Generators and Fuzzers](#payload-generators-and-fuzzers)-字典/payload的生成或FUZZer
- [Cryptography](#cryptography)-加解密相关
- [Tool Integration](#tool-integration)-与burp或其他软件集成的相关插件
- [Misc](#misc)-其他的，未分类的杂项
- [Burp Extension Training Resources](#burp-extension-training-resources)-与开发Burp扩展有帮助的相关博客文章，演讲和幻灯片。

## Scanners

*Passive and Active scan plugins.*

* [ActiveScan++](https://github.com/albinowax/ActiveScanPlusPlus) - ActiveScan++ extends Burp Suite's active and passive scanning capabilities.
* [Burp Vulners Scanner](https://github.com/vulnersCom/burp-vulners-scanner) - Vulnerability scanner based on vulners.com search API.
* [Additional Scanner checks](https://github.com/portswigger/additional-scanner-checks) - Collection of scanner checks missing in Burp.
* [CSRF Scanner](https://github.com/ah8r/csrf) - CSRF Scanner Extension for Burp Suite Pro.
* [HTML5 Auditor](https://github.com/PortSwigger/html5-auditor) - This extension checks for usage of HTML5 features that have potential security risks.
* [Software Version Reporter](https://github.com/augustd/burp-suite-software-version-checks) - Burp extension to passively scan for applications revealing software version numbers.
* [J2EEScan](https://github.com/ilmila/J2EEScan) - J2EEScan is a plugin for Burp Suite Proxy. The goal of this plugin is to improve the test coverage during web application penetration tests on J2EE applications.
* [Java Deserialization Scanner](https://github.com/federicodotta/Java-Deserialization-Scanner) - All-in-one plugin for Burp Suite for the detection and the exploitation of Java deserialization vulnerabilities.
* [CSP Bypass](https://github.com/moloch--/CSP-Bypass) - A Burp Plugin for Detecting Weaknesses in Content Security Policies.
* [Burp Sentinel](https://github.com/dobin/BurpSentinel) - GUI Burp Plugin to ease discovering of security holes in web applications.
* [Backslash Powered Scanner](https://github.com/PortSwigger/backslash-powered-scanner) - Finds unknown classes of injection vulnerabilities. 
* [Collaborator Everywhere](https://github.com/PortSwigger/collaborator-everywhere) - A Burp Suite Pro extension which augments your proxy traffic by injecting non-invasive headers designed to reveal backend systems by causing pingbacks to Burp Collaborator
* [Burp Molly Pack](https://github.com/yandex/burp-molly-pack) - Security checks pack for Burp Suite.
* [Noopener Burp Extension](https://github.com/snoopysecurity/Noopener-Burp-Extension) - Find Target=_blank values within web pages that are set without noopener and noreferrer attributes.
* [ActiveScan3Plus](https://github.com/silentsignal/ActiveScan3Plus) - Modified version of ActiveScan++ Burp Suite extension.
* [Burp Image Size](https://github.com/silentsignal/burp-image-size) - Image size issues plugin for Burp Suite.
* [UUID issues for Burp Suite](https://github.com/silentsignal/burp-uuid) - UUID issues for Burp Suite.
* [JSON array issues for Burp Suite](https://github.com/silentsignal/burp-json-array) - JSON Array issues plugin for Burp Suite.
* [Burp Retire JS](https://github.com/h3xstream/burp-retire-js) - Burp/ZAP/Maven extension that integrate Retire.js repository to find vulnerable Javascript libraries.
* [SOMEtime](https://github.com/linkedin/sometime) - A BurpSuite plugin to detect Same Origin Method Execution vulnerabilities.
* [HTTPoxy Scanner](https://github.com/PortSwigger/httpoxy-scanner) - A Burp Suite extension that checks for the HTTPoxy vulnerability.
* [ParrotNG](https://github.com/ikkisoft/ParrotNG) - ParrotNG is a tool capable of identifying Adobe Flex applications (SWF) vulnerable to CVE-2011-2461.
* [Error Message Checks](https://github.com/augustd/burp-suite-error-message-checks) - Burp Suite extension to passively scan for applications revealing server error messages.
* [Identity Crisis](https://github.com/EnableSecurity/Identity-Crisis) - A Burp Suite extension that checks if a particular URL responds differently to various User-Agent headers.
* [CSP Auditor](https://github.com/GoSecure/csp-auditor) - Burp and ZAP plugin to analyse Content-Security-Policy headers or generate template CSP configuration from crawling a Website/
* [Burp Suite GWT Scan](https://github.com/augustd/burp-suite-gwt-scan) - Burp Suite plugin identifies insertion points for GWT (Google Web Toolkit) requests.
* [Minesweeper](https://github.com/codingo/Minesweeper) - A Burpsuite plugin (BApp) to aid in the detection of scripts being loaded from over 14000+ malicious cryptocurrency mining domains (cryptojacking).
* [Yara](https://portswigger.net/bappstore/11e2ec6923f2497db9c18ec92492c63a) - This extension allows you to perform on-demand Yara scans of websites within the Burp interface based on custom Yara rules that you write or obtain. 
* [WordPress Scanner](https://portswigger.net/bappstore/77a12b2966844f04bba032de5744cd35) - Find known vulnerabilities in WordPress plugins and themes using WPScan database.
* [Web Cache Deception Burp Extension](https://portswigger.net/bappstore/7c1ca94a61474d9e897d307c858d52f0) - This extension tests applications for the Web Cache Deception vulnerability.
* [UUID Detector](https://portswigger.net/bappstore/65f32f209a72480ea5f1a0dac4f38248) - This extension passively reports UUID/GUIDs observed within HTTP requests.
* [SSL Scanner](https://portswigger.net/bappstore/474b3c575a1a4584aa44dfefc70f269d) - This extension enables Burp to scan for SSL vulnerabilities.
* [Software Vulnerability Scanner](https://portswigger.net/bappstore/c9fb79369b56407792a7104e3c4352fb) - This extension scans for vulnerabilities in detected software versions using the Vulners.com API.
* [Reverse Proxy Detector](https://portswigger.net/bappstore/a112997070354d249b64b4cf68eabc04) - This extension detects reverse proxy servers.
* [SRI Check](https://github.com/SolomonSklash/sri-check) - A Burp Suite extension for identifying missing Subresource Integrity attributes.
* [Reflected File Download Checker](https://portswigger.net/bappstore/34cd4392e7e04999b9ca0cc91f58886c) - This extension checks for reflected file downloads.
* [Length Extension Attacks](https://portswigger.net/bappstore/f156669cae8d4c10a3cd9d0b5270bcf6) - his extension lets you perform hash length extension attacks on weak signature mechanisms.
* [Headers Analyzer](https://portswigger.net/bappstore/8b4fe2571ec54983b6d6c21fbfe17cb2) - This extension adds a passive scan check to report security issues in HTTP headers.
* [Heartbleed](https://portswigger.net/bappstore/d405150b57e54887b1dcfa563b7c0b6f) - This extension adds a new tab to Burp's Suite main UI allowing a server to be tested for the Heartbleed bug. If the server is vulnerable, data retrieved from the server's memory will be dumped and viewed.
* [Image Size Issues](https://portswigger.net/bappstore/1b602a9ae78a4ba4bc9f7b2c405a2b4e) - This extension passively detects potential denial of service attacks due to the size of an image being specified in request parameters.
* [CMS Scanner](https://portswigger.net/bappstore/1bf95d0be40c447b94981f5696b1a18e) - An active scan extension for Burp that provides supplemental coverage when testing popular content management systems.
* [Detect Dynamic JS](https://portswigger.net/bappstore/4a657674ebe3410b92280613aa512304) - This extension compares JavaScript files with each other to detect dynamically generated content and content that is only accessible when the user is authenticated.
* [CTFHelper](https://github.com/unamer/CTFHelper) - This extension will scan some sensitive files (backup files likes .index.php.swp or .git directory) in web server that makes solving CTF challenge faster.
* [Broken Link Checker](https://github.com/arbazkiraak/BurpBLH) - This extension discovers the broken links passively could be handy in second order takeovers.  
* [Scan manual insertion point](https://github.com/cnotin/burp-scan-manual-insertion-point) - This Burp extension lets the user select a region of a request (typically a parameter value), and via the context menu do an active scan of just the insertion point defined by that selection.
* [AdminPanelFinder](https://github.com/moeinfatehi/Admin-Panel_Finder) - A burp suite extension that enumerates infrastructure and application Admin Interfaces (OWASP OTG-CONFIG-005).

## Custom Features

*Extensions related to customizing Burp features and extend the functionality of Burp Suite in numerous ways.*

* [Burp Bounty - Scan Check Builder](https://github.com/wagiro/BurpBounty) - This BurpSuite extension allows you, in a quick and simple way, to improve the active and passive burpsuite scanner by means of personalized rules through a very intuitive graphical interface.
* [Scan Manual Insertion Point](https://portswigger.net/bappstore/ca7ee4e746b54514a0ca5059329e926f) - This Burp extension lets the user select a region of a request (typically a parameter value), and via the context menu do an active scan of just the insertion point defined by that selection. 
* [Distribute Damage](https://portswigger.net/bappstore/543ab7a08d954390bd1a5f4253d3763b) - Designed to make Burp evenly distribute load across multiple scanner targets, this extension introduces a per-host throttle and a context menu to trigger scans from. 
* [Add & Track Custom Issues](https://github.com/JAMESM0RR1S/Add-And-Track-Custom-Issues) - This extension allows custom scan issues to be added and tracked within Burp. 
* [Decoder Pro](https://github.com/Matanatr96/DecoderProBurpSuite) - Burp Suite Plugin to decode and clean up garbage response text.
* [Decoder Improved](https://portswigger.net/bappstore/0a05afd37da44adca514acef1cdde3b9) - Decoder Improved is a data transformation plugin for Burp Suite that better serves the varying and expanding needs of information security professionals. 
* [Request Highlighter](https://portswigger.net/bappstore/11729a617d8d4d3b87c82e34b71885c3) - Request Highlighter is a simple extension for Burp Suite tool (for both community and professional editions) that provides an automatic way to highlight HTTP requests based on headers content (eg. Host, User-Agent, Cookies, Auth token, custom headers etc.).
* [Request Minimizer](https://portswigger.net/bappstore/cc16f37549ff416b990d4312490f5fd1) - This extension performs HTTP request minimization. It deletes parameters that are not relevant such as: random ad cookies, cachebusting nonces, etc.
* [Wildcard](https://github.com/hvqzao/burp-wildcard) - There is number of great Burp extension out there. Most of them create their own tabs.
* [Hackvertor](https://github.com/hackvertor/hackvertor) - Hackvertor is a tag-based conversion tool that supports various escapes and encodings including HTML5 entities, hex, octal, unicode, url encoding etc.
* [Multi-Browser Highlighting](https://portswigger.net/bappstore/29fb77b2611d4c27a9a0b8bc504d8ca2) - This extension highlights the Proxy history to differentiate requests made by different browsers. The way this works is that each browser would be assigned one color and the highlights happen automatically.
* [Manual Scan Issues](https://portswigger.net/bappstore/3ebca77f69434faea1e3e97e0269fe17) - This extension allows users to manually create custom issues within the Burp Scanner results.
* [Handy Collaborator](https://portswigger.net/bappstore/dcf7c44cdc7b4698bba86d94c692fb7f) - Handy Collaborator is a Burp Suite Extension that lets you use the Collaborator tool during manual testing in a comfortable way.
* [BadIntent](https://github.com/mateuszk87/BadIntent) - Intercept, modify, repeat and attack Android's Binder transactions using Burp Suite.
* [Custom Send-To](https://github.com/PortSwigger/custom-send-to) - Adds a customizable "Send to..."-context-menu to your BurpSuite.

## Beautifiers and Decoders

*Extensions related to beautifying and decoding data formats.*

* [.NET Beautifier](https://github.com/allfro/dotNetBeautifier) - A BurpSuite extension for beautifying .NET message parameters and hiding some of the extra clutter that comes with .NET web apps (i.e. __VIEWSTATE).
* [JS Beautifier](https://github.com/irsdl/BurpSuiteJSBeautifier) - Burp Suite JS Beautifier 
* [Burp ASN1 Toolbox](https://github.com/silentsignal/burp-asn1) - ASN.1 toolbox for Burp Suite.
* [JSON JTree viewer for Burp Suite](https://github.com/silentsignal/burp-json-jtree) - JSON JTree viewer for Burp Suite.
* [JSON Beautifier](https://github.com/NetSPI/JSONBeautifier) - JSON Beautifier for Burp written in Java
* [Browser Repeater](https://github.com/allfro/browserRepeater) - BurpSuite extension for Repeater tool that renders responses in a real browser.
* [GQL Parser](https://github.com/br3akp0int/GQLParser) - A repository for GraphQL Extension for Burp Suite
* [XChromeLogger Decoder](https://portswigger.net/bappstore/a68f0a880362410baaf884ddb383fe4c) - his extension adds a new tab in the HTTP message editor to display X-ChromeLogger-Data in decoded form.
* [WebSphere Portlet State Decoder](https://portswigger.net/bappstore/49e9917c721e4abfa4c2540b07f35eb7) - This extension displays the decoded XML state of a WebSphere Portlet in a new tab when the request is viewed.
* [PDF Viewer](https://portswigger.net/bappstore/4b0cbd1e44da4212881cc1480ba1bc68) - This extension adds a tab to the HTTP message viewer to render PDF files in responses.
* [NTLM Challenge Decoder](https://portswigger.net/bappstore/30d095e075e64a109b8d12fc8281b5e3) - This extension decodes NTLM SSP headers. 
* [JCryption Handler](https://portswigger.net/bappstore/fe2a5a42985b4ac8b1801a09b670758f) - This extension provides a way to perform manual and/or automatic Security Assessment for Web Applications that using JCryption JavaScript library to encrypt data sent through HTTP methods (GET and POST).
* [JSWS Parser](https://portswigger.net/bappstore/1d1b8fd9be354c64a5887f25fc271e56) - This extension can be used to parse a response containing a JavaScript Web Service Proxy (JSWS) and generate JSON requests for all supported methods.
* [JSON Decoder](https://portswigger.net/bappstore/ceed5b1568ba4b92abecce0dff1e1f2c) - This extension adds a new tab to Burp's HTTP message editor, and displays JSON messages in decoded form.
* [MessagePack](https://portswigger.net/bappstore/c199ec3330864d548ff7d6bf761960ba) - This extension supports: decoding MessagePack requests and responses to JSON format, converting requests from JSON format to MessagePack.
* [Fast Infoset Tester](https://portswigger.net/bappstore/2f640c88e0394bb09e788378f1bcc80f) - This extension converts incoming Fast Infoset requests and responses to XML, and converts outgoing messages back to Fast Infoset. 
* [burp-protobuf-decoder](https://github.com/mwielgoszewski/burp-protobuf-decoder) - A simple Google Protobuf Decoder for Burp
* [BurpAMFDSer](https://github.com/NetSPI/Burp-Extensions/tree/master/BurpAMFDSer) - BurpAMFDSer is a Burp plugin that will deserialze/serialize AMF request and response to and from XML with the use of Xtream library.
* [Deflate Burp Plugin](https://github.com/GDSSecurity/Deflate-Burp-Plugin) - The Deflate Burp Plugin is a plug-in for Burp Proxy (it implements the IBurpExtender interface) that decompresses HTTP response content in the ZLIB (RFC1950) and DEFLATE (RFC1951) compression formats.
* [Burp Suite GWT wrapper](https://github.com/dnet/burp-gwt-wrapper) - Burp Suite GWT wrapper
* [GraphQL Beautifier](https://github.com/zidekmat/graphql_beautifier) - Burp Suite extension to help make Graphql request more readable.
* [Decoder Improved](https://github.com/nccgroup/Decoder-Improved) - Improved decoder for Burp Suite.


## Cloud Security

*Plugins related to assessing Cloud Security services such as Amazon AWS.*

* [AWS Security Checks](https://github.com/PortSwigger/aws-security-checks) - This extensions provides additional Scanner checks for AWS security issues.
* [AWS Extender](https://github.com/VirtueSecurity/aws-extender) - AWS Extender (Cloud Storage Tester) is a Burp plugin to assess permissions of cloud storage containers on AWS, Google Cloud and Azure.
* [AWS Signer](https://github.com/NetSPI/AWSSigner) - Burp Extension for AWS Signing.

## Scripting

*Extensions related to Scripting.*

* [Python Scripter](https://github.com/portswigger/python-scripter) - This extension allows execution of a custom Python script on each HTTP 
request and response processed by Burp.
* [Burpkit](https://github.com/allfro/BurpKit) - BurpKit is a BurpSuite plugin which helps in assessing complex web apps that render the contents of their pages dynamically. 
* [Burp Requests](https://github.com/silentsignal/burp-requests) - Copy as requests plugin for Burp Suite.
* [Burpy](https://github.com/debasishm89/burpy) - Portable and flexible web application security assessment tool.It parses Burp Suite log and performs various tests depending on the module provided and finally generate a HTML report.
* [Buby](https://github.com/tduehr/buby) - A JRuby implementation of the BurpExtender interface for PortSwigger Burp Suite.
* [Burpee](https://github.com/GDSSecurity/burpee) - Python object interface to requests/responses recorded by Burp Suite.
* [Burp Jython Tab](https://github.com/mwielgoszewski/burp-jython-tab) - Description not available.
* [Reissue Request Scripter](https://portswigger.net/bappstore/6e0b53d8c801471c9dc614a016d8a20d) - This extension generates scripts to reissue a selected request. 
* [Burp Buddy](https://github.com/tomsteele/burpbuddy) - burpbuddy exposes Burp Suites's extender API over the network through various mediums, with the goal of enabling development in any language without the restrictions of the JVM.
* [Copy As Python-Requests](https://portswigger.net/bappstore/b324647b6efa4b6a8f346389730df160) - This extension copies selected request(s) as Python-Requests invocations.
* [Copy as PowerShell Requests](https://portswigger.net/bappstore/4da25d602db04f5ca7c4b668e4611cfe) - This extension copies the selected request(s) as PowerShell invocation(s).
* [Copy as Node Request](https://portswigger.net/bappstore/e170472f83ef4da1bca5897203b6b33d) - This extension copies the selected request(s) as Node.JS Request invocations.
* [BReWSki](https://github.com/Burp-BReWSki/BReWSki) - BReWSki (Burp Rhino Web Scanner) is a Java extension for Burp Suite that allows user to write custom scanner checks in JavaScript. 

## OAuth and SSO

*Extensions for assessing Single sign-on (SSO) and OAuth related applications.*

* [SAML Raider](https://github.com/SAMLRaider/SAMLRaider) - SAML Raider is a Burp Suite extension for testing SAML infrastructures. It contains two core functionalities: Manipulating SAML Messages and manage X.509 certificates.
* [Burp OAuth](https://github.com/dnet/burp-oauth) - OAuth plugin for Burp Suite Extender.
* [EsPReSSO](https://github.com/RUB-NDS/BurpSSOExtension) - An extension for BurpSuite that highlights SSO messages in Burp's proxy window..
* [SAML Encoder/Decoder](https://portswigger.net/bappstore/9ff11c976383491b976389ce23091ee3) - This extension adds a new tab to Burp's main UI, allowing encoding and decoding of SAML (Security Assertion Markup Language) formatted messages.
* [SAML Editor](https://portswigger.net/bappstore/32c38cd10ef44c1cbca9d54483f78e88) - This extension adds a new tab to Burp's HTTP message editor, allowing encoding and decoding of SAML (Security Assertion Markup Language) formatted messages.
* [PeopleSoft Token Extractor](https://portswigger.net/bappstore/df04d7d1af004ed6b50c555c4920232d) - This extension help test PeopleSoft SSO tokens.
* [JSON Web Token Attacker](https://portswigger.net/bappstore/82d6c60490b540369d6d5d01822bdf61) - This extension helps to test applications that use JavaScript Object Signing and Encryption, including JSON Web Tokens.
* [JSON Web Tokens](https://portswigger.net/bappstore/f923cbf91698420890354c1d8958fee6) - This extension lets you decode and manipulate JSON web tokens on the fly, check their validity and automate common attacks against them.
* [AuthHeader Updater](https://github.com/sampsonc/AuthHeaderUpdater) - Burp extension to specify the token value for the Authenication header while scanning.

## Information Gathering

*Extensions related to Discovery, Spidering and Information Gathering.*

* [Google Hack](https://portswigger.net/bappstore/a00a906943de49159092e329cc4f95f4) - This extension provides a GUI interface for setting up and running Google Hacking queries, and lets you add results directly to Burp's site map..
* [PwnBack/Wayback Machine](https://github.com/P3GLEG/PwnBack) - Burp Extender plugin that generates a sitemap of a website using Wayback Machine.
* [Directory File Listing Parser Importer](https://github.com/SmeegeSec/Directory_File_Listing_Parser_Importer) - This is a Burp Suite extension in Python to parse a directory and file listing text file of a web application.
* [Site Map Extractor](https://portswigger.net/bappstore/f991b67d4ef94f3c8692c3edca06583e) - This extension extracts information from the Site Map. You can use the full site map or just in-scope items. 
* [Site Map Fetcher](https://portswigger.net/bappstore/93bbecc3da434ef7ba5a5b2b98265169) - This extension fetches the responses of unrequested items in the site map.
* [Burp CSJ](https://portswigger.net/bappstore/371cebe47d8d4049a92dc03b66e1105f) - This extension integrates Crawljax, Selenium and JUnit together. The intent of this extension is to aid web application security testing, increase web application crawling capability and speed-up complex test-cases execution.
* [Attack Surface Detector](https://portswigger.net/bappstore/47027b96525d4353aea5844781894fb1) - The Attack Surface Detector uses static code analyses to identify web app endpoints by parsing routes and identifying parameters.
* [domain_hunter](https://github.com/bit4woo/domain_hunter) - A Burp Suite extender that try to find sub-domains,similar domains and related domains of an organization, not only domain.
* [BigIP Discover](https://github.com/raise-isayan/BigIPDiscover) - A extension of Burp suite. The cookie set by the BipIP server may include a private IP, which is an extension to detect that IP
* [AdminPanelFinder](https://github.com/moeinfatehi/Admin-Panel_Finder) - A burp suite extension that enumerates infrastructure and application Admin Interfaces (OWASP OTG-CONFIG-005).
* [Asset Discover](https://github.com/redhuntlabs/BurpSuite-Asset_Discover) - Burp Suite extension to discover assets from HTTP response using passive scanning.
## Vulnerability Specific Extensions

### Cross-site scripting
* [XSS Validator](https://github.com/nVisium/xssValidator) - This is a burp intruder extender that is designed for automation and validation of XSS vulnerabilities.
* [burp-xss-sql-plugin](https://github.com/attackercan/burp-xss-sql-plugin) - Publishing plugin which I used for years which helped me to find several bugbounty-worthy XSSes, OpenRedirects and SQLi.
* [Burp Hunter](https://github.com/mystech7/Burp-Hunter) - XSS Hunter Burp Plugin.
* [DOM XSS Checks](https://www.codemagi.com/downloads/private/9982e094925d19aa1b122da5f1dbcd86/DOMXSSChecks.zip) - This Burp Suite plugin passively scans for DOM-Based Cross-Site Scripting. 
* [Reflector](https://github.com/elkokc/reflector) - Burp plugin able to find reflected XSS on page in real-time while browsing on site
* [BitBlinder](https://github.com/BitTheByte/BitBlinder) - Burp extension helps in finding blind xss vulnerabilities

### Server-Side-Request-Forgery
> 相关资料：1.https://ctf-wiki.github.io/ctf-wiki/web/ssrf/  |  2.https://xz.aliyun.com/t/2115

### Broken Access Control
* [Burplay/Multi Session Replay](https://github.com/SpiderLabs/burplay) - Burplay is a Burp Extension allowing for replaying any number of requests using same modifications definition. Its main purpose is to aid in searching for Privilege Escalation issues.
* [AuthMatrix](https://github.com/SecurityInnovation/AuthMatrix) - AuthMatrix is a Burp Suite extension that provides a simple way to test authorization in web applications and web services.
* [Autorize](https://github.com/Quitten/Autorize) - Automatic authorization enforcement detection extension for burp suite written in Jython developed by Barak Tawily in order to ease application security people work and allow them perform an automatic authorization tests.
* [AutoRepeater](https://github.com/nccgroup/AutoRepeater) - Automated HTTP Request Repeating With Burp Suite.
* [UUID issues for Burp Suite](https://github.com/silentsignal/burp-uuid) - UUID issues for Burp Suite.
* [Authz](https://github.com/wuntee/BurpAuthzPlugin) - Burp plugin to test for authorization flaws.
* [Paramalyzer](https://github.com/JGillam/burp-paramalyzer) - Paramalyzer - Burp extension for parameter analysis of large-scale web application penetration tests.
* [Burp SessionAuth](https://github.com/thomaspatzke/Burp-SessionAuthTool) - Burp plugin which supports in finding privilege escalation vulnerabilities.
* [Auto Repeater](https://portswigger.net/bappstore/f89f2837c22c4ab4b772f31522647ed8) - This extension automatically repeats requests, with replacement rules and response diffing. It provides a general-purpose solution for streamlining authorization testing within web applications.
* [IncrementMe Please](https://github.com/alexlauerman/IncrementMePlease) - Burp extension to increment a parameter in each active scan request.

### Cross-Site Request Forgery
* [CSRF Scanner](https://github.com/ah8r/csrf) -  CSRF Scanner Extension for Burp Suite Pro.
* [CSurfer](https://github.com/asaafan/CSurfer) - CSurfer is a CSRF guard hiding extension that keeps track of the latest guard value per session and update new requests accordingly.
* [Additional CSRF Checks/EasyCSRF](https://github.com/0ang3el/EasyCSRF) - EasyCSRF helps to find weak CSRF-protection in WebApp which can be easily bypassed. 
* [Match/Replace Session Action](https://portswigger.net/bappstore/9b5c532966ca4d5eb13c09c72ba7aac2) - This extension provides match and replace functionality as a Session Handling Rule.
* [Token Extractor](https://portswigger.net/bappstore/f24211fa6fcd4bbea6b21f99c5cad27a) - This extension allows tokens to be extracted from a response and replaced in requests.
* [CSRF Token Tracker](https://portswigger.net/bappstore/61ddd8a0464544218dfd94114c910548) - This extension provides a sync function for CSRF token parameters.
* [Token Rewrite](https://github.com/hvqzao/burp-token-rewrite) - This extension lets you search for specific values like CSRF tokens in responses and use their values to modify parameters in future requests or set a cookie.

### Deserialization
* [Java-Deserialization-Scanner](https://github.com/federicodotta/Java-Deserialization-Scanner) - All-in-one plugin for Burp Suite for the detection and the exploitation of Java deserialization vulnerabilities.
* [Java Serial Killer](https://github.com/NetSPI/JavaSerialKiller) - Burp extension to perform Java Deserialization Attacks.
* [BurpJDSer-ng](https://github.com/IOActive/BurpJDSer-ng) - Allows you to deserialize java objects to XML and lets you dynamically load classes/jars as needed.
* [PHP Object Injection Check](https://portswigger.net/bappstore/24dab228311049d89a27a4d721e17ef7) - This extension adds an active scan check to find PHP object injection vulnerabilities..
* [Java Serialized Payloads](https://portswigger.net/bappstore/bc737909a5d742eab91544705c14d34f) - This extension generates various Java serialized payloads designed to execute OS commands..
* [Freddy, Deserialization Bug Finder](https://portswigger.net/bappstore/ae1cce0c6d6c47528b4af35faebc3ab3) - Helps with detecting and exploiting serialization libraries/APIs.
* [CustomDeserializer](https://portswigger.net/bappstore/84ff4dceaae14e84990c6f3f7fe999bd) - This extension speeds up manual testing of web applications by performing custom deserialization.
* [BurpJDSer](https://github.com/NetSPI/Burp-Extensions/tree/master/BurpJDSer) - BurpJDSer is a Burp plugin that will deserialze/serialize Java request and response to and from XML with the use of Xtream library.

### Sensitive Data Exposure
* [Burp Smart Buster](https://github.com/pathetiq/BurpSmartBuster) - A Burp Suite content discovery plugin that add the smart into the Buster!.
* [PDF Metadata](https://github.com/luh2/PDFMetadata) - The PDF Metadata Burp Extension provides an additional passive Scanner check for metadata in PDF files.
* [SpyDir](https://github.com/aur3lius-dev/SpyDir) - BurpSuite extension to assist with Automated Forced Browsing/Endpoint Enumeration.
* [Burp Hash](https://github.com/burp-hash/burp-hash) - Many applications will hash parameters such as ID numbers and email addresses for use in secure tokens, like session cookies. 
* [Param Miner](https://portswigger.net/bappstore/17d2949a985c4b7ca092728dba871943) - This extension identifies hidden, unlinked parameters. It's particularly useful for finding web cache poisoning vulnerabilities.
* [MindMap Exporter](https://portswigger.net/bappstore/676b2e91c5a347289fca66fa67cca545) - Aids with documentation of the following OWASP Testing Guide V4 tests: OTG-INFO-007: Map execution paths through application, OTG-INFO-006: Identify application entry points.
* [Image Location & Privacy Scanner](https://portswigger.net/bappstore/f3aec37088aa494c81962d965219be46) - Passively scans for GPS locations or embedded privacy related exposure (like camera serial numbers) in images during normal security assessments of websites via a Burp plug-in.
* [Image Metadata](https://portswigger.net/bappstore/3996aa01e0474b1a990db586a7f14ab7) - This extension extract metadata present in image files. The information found is rarely critical, but it can be useful for general reconnaissance. These information can be usernames who created the files, local paths and technologies used.
* [ExifTool Scanner](https://portswigger.net/bappstore/858352a27e6e4a6caa802e61fdeb7dd4) - This Burp extension reads metadata from various filetypes (JPEG, PNG, PDF, DOC, XLS and much more) using ExifTool. Results are presented as Passive scan issues and Message editor tabs.
* [Interesting Files Scanner](https://github.com/modzero/interestingFileScanner) - Interesting Files Scanner extends Burp Suite's active scanner, with scans for interesting files and directories. A main feature of the extension is the check for false positives with tested patterns for each case. 

### SQL Injection
* [CO2](https://github.com/JGillam/burp-co2) - A collection of enhancements for Portswigger's popular Burp Suite web penetration testing tool.
* [SQLiPy](https://github.com/codewatchorg/sqlipy) - SQLiPy is a Python plugin for Burp Suite that integrates SQLMap using the SQLMap API.
* [burp-xss-sql-plugin](https://github.com/attackercan/burp-xss-sql-plugin) - ublishing plugin which I used for years which helped me to find several bugbounty-worthy XSSes, OpenRedirects and SQLi.
* [SQLiPy Sqlmap Integration](https://portswigger.net/bappstore/f154175126a04bfe8edc6056f340f52e) - This extension integrates Burp Suite with SQLMap.
* [InjectMate](https://github.com/laconicwolf/burp-extensions/blob/master/InjectMate.py) - Burp Extension that generates payloads for XSS, SQLi, and Header injection vulns
### XXE
* [Office OpenXML Editor](https://github.com/PortSwigger/office-open-xml-editor) - Burp extension that add a tab to edit Office Open XML document (xlsx,docx,pptx).
* [Content Type Converter](https://github.com/NetSPI/Burp-Extensions/tree/master/ContentTypeConverter) - Burp extension to convert XML to JSON, JSON to XML, x-www-form-urlencoded to XML, and x-www-form-urlencoded to JSON.

### Insecure File Uploads
* [HTTP file upload scanner](https://github.com/modzero/mod0BurpUploadScanner) - A Burp Suite Pro extension to do security tests for HTTP file uploads.
* [ZIP File Raider](https://github.com/destine21/ZIPFileRaider) - Burp Extension for ZIP File Payload Testing.
* [File Upload Traverser](https://portswigger.net/bappstore/5f46fe766e9c435992c610160bb53cba) - This extension verifies if file uploads are vulnerable to directory traversal vulnerabilities. 

### Directory Traversal
* [Uploader](https://github.com/thec00n/Uploader) - Burp extension to test for directory traversal attacks in insecure file uploads.
* [off-by-slash](https://github.com/bayotop/off-by-slash) - Burp extension to detect alias traversal via NGINX misconfiguration at scale.

### Session Management
* [WAFDetect](https://portswigger.net/bappstore/12bef6b7607e46cf965c16f76e905a4c) - This extension passively detects the presence of a web application firewall (WAF) from HTTP responses.
* [TokenJar](https://portswigger.net/bappstore/d9e05bf81c8f4bae8a5b0b01955c5578) - This extension provides a way of managing tokens like anti-CSRF, CSurf, Session IDs.
* [Token Incrementor](https://portswigger.net/bappstore/ae166662024149f981bb6920cf3c8960) - A simple but useful extension to increment a parameter in each request, intended for use with Active Scan.
* [Token Extractor](https://portswigger.net/bappstore/f24211fa6fcd4bbea6b21f99c5cad27a) - This extension allows tokens to be extracted from a response and replaced in requests. 
* [Session Auth](https://portswigger.net/bappstore/9cbdeea2d3744e5ab0f2d08632438985) - This extension can be used to identify authentication privilege escalation vulnerabilities.
* [Session Timeout Test](https://portswigger.net/bappstore/c4bfd29882974712a1d69c6d8f05874e) - This extension attempts to determine how long it takes for a session to timeout at the server. 
* [Session Tracking Checks](https://portswigger.net/bappstore/1ab99dc6b61b45469759fdc38f371278) - This extension checks for the presence of known session tracking sites.
* [ExtendedMacro](https://portswigger.net/bappstore/33839d04fdaa4e3b80292fbed115db13) - This extension provides a similar but extended version of the Burp Suite macro feature.
* [AuthHeader Updater](https://github.com/sampsonc/AuthHeaderUpdater) - Burp extension to specify the token value for the Authenication header while scanning. 
* [Request Randomizer](https://portswigger.net/bappstore/36d6d7e35dac489b976c2f120ce34ae2) - This extension registers a session handling rule which places a random value into a specified location within requests.
* [BearerAuthToken](https://github.com/twelvesec/BearerAuthToken) - This burpsuite extender provides a solution on testing Enterprise applications that involve security Authorization tokens into every HTTP requests.
* [Burp Wicket Handler](https://github.com/Meatballs1/burp_wicket_handler/tree/8047692597e837de02810b5ef3ad97ed0da1385a) - Used as part of Burps Session Handling, Record a Macro which just gets the page you want to submit
* [Add Request to Macro](https://github.com/pajswigger/add-request-to-macro) - This Burp extension lets you add a request to an existing macro.

### Command Injection

* [Command Injection Attacker/Shelling](https://github.com/portswigger/command-injection-attacker) - a comprehensive OS command injection payload generator.
* [Argument Injection Hammer](https://github.com/nccgroup/argumentinjectionhammer) - it is used to identify argument injection vulnerabilities, like *curl* *awk* etc, and sth just like these.

## Web Application Firewall Evasion

*The following extensions can aid during WAF evasion.*

* [Bypass Waf](https://github.com/codewatchorg/bypasswaf) - Add headers to all Burp requests to bypass some WAF products.
* [Random IP Address Header](https://github.com/PortSwigger/random-ip-address-header) - This extension automatically generates IPV6 and IPV4 fake source address headers to evade WAF filtering.
* [Burp Suite HTTP Smuggler](https://github.com/nccgroup/BurpSuiteHTTPSmuggler/) - A Burp Suite extension to help pentesters to bypass WAFs or test their effectiveness using a number of techniques.
* [What-The-WAF](https://portswigger.net/bappstore/5da470c526ea4661a82187ec3e0f94aa) - This extension adds a custom payload type to the Intruder tool, to help test for bypasses of Web Application Firewalls (WAFs).
* [WAF Cookie Fetcher](https://portswigger.net/bappstore/0f6ce51c1cb349689ecb4025e8db060a) - This extension allows web application security testers to register various types of cookie-related session handling actions to be performed by the Burp session handling rules.
* [WAFDetect](https://portswigger.net/bappstore/12bef6b7607e46cf965c16f76e905a4c) - This extension passively detects the presence of a web application firewall (WAF) from HTTP responses.
* [LightBulb WAF Auditing Framework](https://portswigger.net/bappstore/3144e67e904a4fdf91ea96cf4c694c39) - LightBulb is an open source python framework for auditing web application firewalls and filters.
* [BurpSuiteHTTPSmuggler](https://github.com/nccgroup/BurpSuiteHTTPSmuggler) - A Burp Suite extension to help pentesters to bypass WAFs or test their effectiveness using a number of techniques.
* [Chunked coding converter](https://github.com/c0ny1/chunked-coding-converter) - This entension use a Transfer-Encoding technology to bypass the waf.

## Logging and Notes

*Extensions related to logging HTTP traffic during assessments and storing Burp traffic.*

* [Burp Notes](https://github.com/SpiderLabs/BurpNotesExtension) - Burp Notes Extension is a plugin for Burp Suite that adds a Notes tab. The tool aims to better organize external files that are created during penetration testing..
* [Logger++](https://github.com/nccgroup/BurpSuiteLoggerPlusPlus) - Burp Suite Logger++: Log activities of all the tools in Burp Suite.
* [Burp Dump](https://github.com/crashgrindrips/burp-dump) - A Burp plugin to dump HTTP(S) requests/responses to a file system.
* [Burp SQLite logger](https://github.com/silentsignal/burp-sqlite-logger) - SQLite logger for Burp Suite.
* [Burp Git Version](https://github.com/silentsignal/burp-git-version) - Description not available.
* [Burp Commentator](https://github.com/silentsignal/burp-commentator) - Generates comments for selected request(s) based on regular expressions.
* [Burp Suite Importer](https://github.com/SmeegeSec/Burp-Importer) - Connect to multiple web servers while populating the sitemap.
* [Burp Replicator](https://github.com/portswigger/replicator) - Burp extension to help developers replicate findings from pen tests.
* [Notes](https://portswigger.net/bappstore/b150353ea3d54f61bdc482a4a8470356) - This extension adds a new tab to Burp's UI, for taking notes and organizing external files that are created during penetration testing.
* [Log Requests to SQLite](https://portswigger.net/bappstore/d916d94506734f3490e49391595d8747) - This extension keeps a trace of every HTTP request that has been sent via BURP, in an SQLite database. This is useful for keeping a record of exactly what traffic a pen tester has generated.
* [Flow](https://portswigger.net/bappstore/ee1c45f4cc084304b2af4b7e92c0a49d) - This extension provides a Proxy history-like view along with search filter capabilities for all Burp tools.
* [Custom Logger](https://portswigger.net/bappstore/f5ca4f46dc37424c9666845a6ad0ecef) - This extension adds a new tab to Burp's main UI containing a simple log of all requests made by all Burp tools.
* [Log Requests to SQLite](https://github.com/righettod/log-requests-to-sqlite) - BURP extension to record every HTTP request send via BURP and create an audit trail log of an assessment.
* [Burp Response Clusterer](https://github.com/modzero/burp-ResponseClusterer) - Burp plugin that clusters responses to show an overview of received responses.
* [Burp Collect500](https://github.com/floyd-fuh/burp-Collect500) - Burp plugin that collects all HTTP 500 messages.
* [Sink Logger](https://github.com/bayotop/sink-logger) - Sink Logger is a Burp Suite Extension that allows to transparently monitor various JavaScript sinks. .

## Payload Generators and Fuzzers

*Wordlist/payload generators and fuzzers.*

* [CO2](https://github.com/JGillam/burp-co2) - A collection of enhancements for Portswigger's popular Burp Suite web penetration testing tool.
* [Bradamsa](https://github.com/ikkisoft/bradamsa) - Burp Suite extension to generate Intruder payloads using Radamsa.
* [Payload Parser](https://github.com/infodel/burp.extension-payloadparser) - Burp Extension for parsing payloads containing/excluding characters you provide.
* [Burp Luhn Payload Processor](https://github.com/EnableSecurity/burp-luhn-payload-processor) - A plugin for Burp Suite Pro to work with attacker payloads and automatically generate check digits for credit card numbers and similar numbers that end with a check digit generated using the Luhn algorithm or formula (also known as the "modulus 10" or "mod 10" algorithm)..
* [Gather Contacts](https://github.com/clr2of8/GatherContacts) - A Burp Suite Extension to pull Employee Names from Google and Bing LinkedIn Search Results.
* [Blazer](https://github.com/ikkisoft/blazer) - Burp Suite AMF Extension.
* [Wordlist Extractor](https://portswigger.net/bappstore/21df56baa03d499c8439018fe075d3d7) - Scrapes all unique words and numbers for use with password cracking.
* [PsychoPATH](https://portswigger.net/bappstore/554059e593ce446585574b92344b9675) - This extension provides a customizable payload generator, suitable for detecting a variety of file path vulnerabilities in file upload and download functionality.
* [Meth0dMan](https://portswigger.net/bappstore/8ba6e98e367e40c79824f562f22d2221) - This extension helps with testing HTTP methods. It generates custom Burp Intruder payloads based on the site map, allowing quick identification of several HTTP method issues.
* [Intruder File Payload Generator](https://portswigger.net/bappstore/880cf2cf689b4067afd9db8e2aefb8ba) - This extension provides a way to use file contents and filenames as Intruder payloads.
* [Intruder Time Payloads](https://portswigger.net/bappstore/ad5f51b515d14490ae8842ce61f60df5) - This extension lets you include the current epoch time in Intruder payloads.
* [reCAPTCHA](https://github.com/bit4woo/reCAPTCHA.git) - A burp plugin that automatically recognizes the graphics verification code and is used for Payload in Intruder.
* [Virtual Host Payload Generator](https://github.com/righettod/virtualhost-payload-generator) - Burp extension providing a set of values for the HTTP request Host header for the Burp Intruder in order to abuse virtual host resolution.
* [Stepper](https://github.com/CoreyD97/Stepper) - Stepper is designed to be a natural evolution of Burp Suite's Repeater tool, providing the ability to create sequences of steps and define regular expressions to extract values from responses which can then be used in subsequent steps.
* [Turbo Intruder](https://github.com/PortSwigger/turbo-intruder) - Turbo Intruder is a Burp Suite extension for sending large numbers of HTTP requests and analyzing the results.

## Cryptography

*Extensions related to decryption of encrypted traffic and crypto related attacks.*

* [WhatsApp Protocol Decryption Burp Tool](https://github.com/romanzaikin/BurpExtension-WhatsApp-Decryption-CheckPoint) - This tool was created during our research on Whatsapp Protocol.
* [AES Burp/AES Payloads](https://github.com/lgrangeia/aesburp) - Burp Extension to manipulate AES encrypted payloads.
* [Crypto Attacker](https://github.com/PortSwigger/crypto-attacker) - The extension helps detect and exploit some common crypto flaws.
* [AES Killer](https://github.com/Ebryx/AES-Killer) - Burp plugin to decrypt AES Encrypted traffic of mobile apps on the fly.
* [Length Extension Attacks](https://portswigger.net/bappstore/f156669cae8d4c10a3cd9d0b5270bcf6) - This extension lets you perform hash length extension attacks on weak signature mechanisms.
* [TLS-Attacker-BurpExtension](https://github.com/RUB-NDS/TLS-Attacker-BurpExtension) - The extension is based on the TLS-Attacker and developed by the Chair for Network and Data Security from the Ruhr-University Bochum to assist pentesters and security researchers in the evaluation of TLS Server configurations with Burp Suite.

## Web Services

*Extensions useful for assessing Web Services*

* [WCF-Binary-SOAP-Plug-In](https://github.com/GDSSecurity/WCF-Binary-SOAP-Plug-In) - This is a Burp Suite plug-in designed to encode and decode WCF Binary Soap request and response data ("Content-Type: application/soap+msbin1).
* [WSDL Wizard](https://github.com/SmeegeSec/WSDLWizard) - WSDL Wizard is a Burp Suite plugin written in Python to detect current and discover new WSDL (Web Service Definition Language) files.
* [BurpWCFDSer](https://github.com/NetSPI/Burp-Extensions/tree/master/BurpWCFDser) - BurpWCFDSer is a Burp plugin that will deserialze/serialize WCF request and response to and from XML. 
* [JSWS](https://github.com/NetSPI/JSWS) - Burp Extenstion to parse JavaScript WebService Proxies and create sample requests.
* [JSON Decoder](https://github.com/PortSwigger/json-decoder) - This extension adds a new tab to Burp's HTTP message editor, and displays JSON messages in decoded form.
* [WSDLer](https://github.com/NetSPI/Wsdler) - WSDL Parser extension for Burp.
* [POST2JSON](https://github.com/cyberisltd/POST2JSON/tree/3d6109a4749352849e5e7f27737e5384f78c4552) - Burp Suite Extension to convert a POST request to JSON message, moving any .NET request verification token to HTTP headers if present.
* [WCF Deserializer](https://portswigger.net/bappstore/1ddd8919e946459f9c1bb47eedb19376) - This extension allows Burp to view and modify binary SOAP objects.
* [Postman Integration](https://portswigger.net/bappstore/6ae9ede3630949748842a43518e840a7) - This extension integrates with the Postman tool by generating a Postman collection JSON file.
* [OpenAPI Parser](https://portswigger.net/bappstore/6bf7574b632847faaaa4eb5e42f1757c) - Parse OpenAPI specifications, previously known as Swagger specifications, into the BurpSuite for automating RESTful API testing – approved by Burp for inclusion in their official BApp Store.
* [Content Type Converter](https://github.com/NetSPI/Burp-Extensions/tree/master/ContentTypeConverter) - Burp extension to convert XML to JSON, JSON to XML, x-www-form-urlencoded to XML, and x-www-form-urlencoded to JSON.
* [Burp Non HTTP Extension](https://github.com/summitt/Burp-Non-HTTP-Extension) - Non-HTTP Protocol Extension (NoPE) Proxy and DNS for Burp Suite.
* [Swurg](https://github.com/AresS31/swurg) - Swurg is a Burp Suite extension designed for OpenAPI testing.

## Tool Integration

*Extensions related to integrating Burp Suite with other software/tools.* 

* [Report To Elastic Search](https://portswigger.net/bappstore/8493f7ae00aa4e01b6ffbbd1b8381ccc) - This extension passes along issues discovered by Burp to either stdout or an ElasticSearch database.
* [Qualys WAS](https://portswigger.net/bappstore/3b0105b95e4645a7929faa0cbda1df28) - The Qualys WAS Burp extension provides a way to easily push Burp scanner findings to the Web Application Scanning (WAS) module within the Qualys Cloud Platform. 
* [NMAP Parser](https://portswigger.net/bappstore/0780c0a9f12e47848a94ac3e43dccbd9) - This extension provides a GUI interface for parsing Nmap output files, and adding common web application ports to Burp's target scope.
* [WebInspect Connector](https://github.com/portswigger/webinspect-connector) - Binary-only repository for the HP WebInspect Connector, authored by HP.
* [Faraday](https://portswigger.net/bappstore/82f3cbaea46c4f158fd85bbccc90c31c) - This extension integrates Burp with the Faraday Integrated Penetration-Test Environment.
* [Git Bridge](https://portswigger.net/bappstore/ae94d3ff6007497d863313fdded20daa) - This extension lets Burp users store Burp data and collaborate via git. Users can right-click supported items in Burp to send them to a git repo and use the Git Bridge tab to send items back to the originating Burp tools.
* [Issue Poster](https://portswigger.net/bappstore/5e1ec745965b4e768d1f4908cc5cf22d) - This extension can be used to post details of discovered Scanner issues to an external web service.
* [Code Dx](https://portswigger.net/bappstore/03b096411fed48e49ccf585659650348) - This extension uploads scan reports directly to CodeDx, a software vulnerability correlation and management system.
* [ElasticBurp](https://portswigger.net/bappstore/67f5c31f93d04ad3a3b0a1808b3648fa) - This extension stores requests and responses from selected Burp tools in an ElasticSearch index including metadata like headers and parameters.
* [Dradis Framework](https://portswigger.net/bappstore/c1be8787ebdd45f58c091f6ae30f1af2) - This extension integrates Burp with the Dradis Framework.
* [Burp Dirbuster](https://github.com/vulnersCom/burp-Dirbuster) - Dirbuster plugin for Burp Suite.
* [Pcap Importer](https://portswigger.net/bappstore/01da4fdd9f6e4e12b0622fbdaa2dd26d) - This extension enables Pcap and Pcap-NG files to be imported into the Burp Target site map, and passively scanned.
* [Brida](https://github.com/federicodotta/Brida) - Brida is a Burp Suite Extension that, working as a bridge between Burp Suite and Frida, lets you use and manipulate applications’ own methods while tampering the traffic exchanged between the applications and their back-end services/servers.
* [Burp Chat](https://portswigger.net/bappstore/1d0986521ace4b2dbf0b70836efa999d) - This extension enables collaborative usage of Burp using XMPP/Jabber. You can send items between Burp instances by connecting over a chat session.

## Misc

* [Burp Rest API](https://github.com/vmware/burp-rest-api) - REST/JSON API to the Burp Suite security tool.
* [Burpa](https://github.com/0x4D31/burpa) - A Burp Suite Automation Tool.
* [CVSS Calculator](https://portswigger.net/bappstore/e2209cdad8474342a695b2e279c294f0) - This extension calculates CVSS v2 and v3 scores of vulnerabilities.
* [Burp Uniqueness](https://github.com/silentsignal/burp-uniqueness) - Uniqueness plugin for Burp Suite.
* [Sample Burp Suite extension: custom scanner checks](https://github.com/PortSwigger/example-scanner-checks) - Sample Burp Suite extension: custom scanner checks
* [Burp Bing translator](https://github.com/yehgdotnet/burp-extention-bing-translator) - Testing non-English web apps is pretty straight forward which you can just use browser extension to translate what you see on screens. 
* [Similar Request Excluder](https://github.com/tijme/similar-request-excluder) - A Burp Suite extension that automatically marks similar requests as 'out-of-scope'. 
* [jython-burp-api](https://github.com/mwielgoszewski/jython-burp-api) - Develop Burp extensions in Jython.
* [Jython Burp Extensions](https://github.com/mwielgoszewski/jython-burp-extensions) - Description not available.
* [Add Custom Header](https://github.com/lorenzog/burpAddCustomHeader) - A Burp Suite extension to add a custom header (e.g. JWT).
* [ThreadFix](https://portswigger.net/bappstore/0b0100a98b1c4a0e927f34eac9d01afe) - This extension provides an interface between Burp and ThreadFix.
* [Target Redirector](https://portswigger.net/bappstore/d938ed20acbe4cd9889aa06bd23ba7e1) - This extension allows you to redirect requests to a particular target by replacing an incorrect target hostname/IP with the intended one. The Host header can optionally also be updated.
* [Similar Request Excluder](https://portswigger.net/bappstore/9ecd51851baf4ae6b69c6a951257387a) - Similar Request Excluder is an extension that enables you to automatically reduce the target scope of your active scan by excluding similar (and therefore redundant) requests.
* [Request Timer](https://portswigger.net/bappstore/56675bcf2a804d3096465b2868ec1d65) - This extension captures response times for requests made by all Burp tools. It could be useful in uncovering potential timing attacks.
* [Response Clusterer](https://portswigger.net/bappstore/e63f09f290ad4d9ea20031e84767b303) - This extension clusters similar responses together, and shows a summary with one request/response per cluster. This allows the tester to get an overview of the tested website's responses from all Burp Suite tools.
* [Hackbar](https://github.com/d3vilbug/HackBar) - HackBar plugin for Burpsuite v1.0.
* [HUNT](https://github.com/bugcrowd/HUNT) - HUNT Suite is a collection of Burp Suite Pro/Free and OWASP ZAP extensions. Identifies common parameters vulnerable to certain vulnerability classes (Burp Suite Pro and OWASP ZAP). Organize testing methodologies (Burp Suite Pro and Free).
* [Replicator](https://portswigger.net/bappstore/56cf924977874104ac35e52962a9a553) - Replicator helps developers to reproduce issues discovered by pen testers.
* [Kerberos Authentication](https://portswigger.net/bappstore/94135ed444c84cc095c72e6520bcc583) - This extension provides support for performing Kerberos authentication. This is useful for testing in a Windows domain when NTLM authentication is not supported. 
* [JVM Property Editor](https://portswigger.net/bappstore/150c653f60b54b4eb556ca289a6aa800) - This extension allows the user to view and modify JVM system properties while Burp is running.
* [Lair](https://portswigger.net/bappstore/16ac195454f8429baac1c5357b0d3952) - This extension provides the facility to send Burp Scanner issues directly to a remote Lair project.
* [Google Authenticator](https://portswigger.net/bappstore/fb3685f958f8424493945c6c60c0920c) - This Burp Suite extension turns Burp into a Google Authenticator client. 
* [GWT Insertion Points](https://portswigger.net/bappstore/a0740678763a4c748bbe7c79151cbe00) - This extension automatically identifies insertion points for GWT (Google Web Toolkit) requests when sending them to the active Scanner or Burp Intruder.
* [Headless Burp](https://portswigger.net/bappstore/d54b11f7af3c4dfeb6b81fb5db72e381) - This extension allows you to run Burp Suite's Spider and Scanner tools in headless mode via the command-line.
* [HTTP Mock](https://portswigger.net/bappstore/42680f96fc214513bc5211b3f25fd98b) - This Burp extension provides mock responses that can be customized, based on the real ones.
* [Carbonator](https://portswigger.net/bappstore/e3a26fff8e1d401dade52f3a8d42d06b) - This extension provides a command-line interface to automate the process of configuring target scope, spidering and scanning.
* [Batch Scan Report Generator](https://portswigger.net/bappstore/bc4ad87282e64fc4b35e9b9b05bac1dd) - This extension can be used to generate multiple scan reports by host with just a few clicks.
* [Decompressor](https://portswigger.net/bappstore/ef36a66ebeb04412a52ffc17c2f5e15e) - Often, HTTP traffic is compressed by the server before it is sent to the client in order to reduce network load.
* [Custom Parameter Handler](https://portswigger.net/bappstore/a0c0cd68ab7c4928b3bf0a9ad48ec8c7) - This extension provides a simple way to modify any part of an HTTP message, allowing manipulation with surgical precision even (and especially) when using macros. 
* [CFURL Cache inspector for Burp Suite](https://github.com/silentsignal/burp-cfurl-cache) - CFURL Cache inspector for Burp Suite.
* [Proxy Auto Config](https://portswigger.net/bappstore/7b3eae07aa724196ab85a8b64cd095d1) - This extension automatically configures Burp upstream proxies to match desktop proxy settings.
* [Proxy Action Rules](https://portswigger.net/bappstore/01376d8325c846b988730e9417016039) - This extension can automatically forward, intercept, and drop proxy requests while actively displaying proxy log information and centralizing list management. 
* [Perfmon](https://github.com/sampsonc/Perfmon) - Perfmon is an extension for Burp Suite that shows information about threads, memory being used, and memory allocated.
* [Unicode To Chinese](https://github.com/bit4woo/u2c) - A burpsuite Extender That Convert Unicode To Chinese.
* [Curlit](https://github.com/faffi/curlit/tree/b5cf116d4716376e36cb0e522bdfe90915a7a961) - Burp Python plugin to turn requests into curl commands.
## Burp Extension Training Resources

*Useful blog posts, talks and slides related to developing Burp extensions.*

* [Burp plugin development for java n00bs - Marc Wickenden](https://www.slideshare.net/marcwickenden/burp-plugin-development-for-java-n00bs-44-con)
* [Developing Burp Suite Extensions - Doyensec](https://github.com/doyensec/burpdeveltraining)
* [Writing your first Burp Suite extension - Portswigger](https://portswigger.net/burp/extender/writing-your-first-burp-suite-extension)
* [Burp Extension Writing Workshop - Sanoop Thomas](https://devilslab.in/files/Burp%20Extension%20Writing%20Workshop.pdf)
* [Extending Burp with Python](https://www.owasp.org/images/9/9f/Extending-Burp-with-Python.pptx)
* [Creating Burp Extensions in Python](https://blog.stalkr.net/2015/04/creating-burp-extensions-in-python.html)
* [Burp Extensions in Python and Pentesting Custom Webservices - Neohapsis](https://labs.neohapsis.com/2013/09/16/burp-extensions-in-python-pentesting-custom-web-services/)
* [Writing Burp Suite Marcos and Plugins - Pluralsight](https://www.pluralsight.com/courses/writing-burp-suite-macros-plugins)
* [Extending Burp with Extensions - Chris Bush](http://blog.opensecurityresearch.com/2014/03/extending-burp.html)
* [Burp Suite Extension Development series - Prakhar Prasad](https://prakharprasad.com/burp-suite-extension-development-series/)
* [BSidesCHS 2015: Building Burp Extensions - Jason Gillam](https://www.youtube.com/watch?v=v7Yjdi9NvOY)
* [Intro to Burp Extender Jython - nVisium](https://www.youtube.com/watch?v=4f05lNULX1I)
* [Intro to Burp Extender Java - nVisium](https://www.youtube.com/watch?v=wR1ENja0lI0)
* [Web Penetration Testing with Burp and the CO2 Extension - Jason Gillam](https://www.youtube.com/watch?v=ez9KSqlYoWU)
* [Developing Burp Suite Extensions with Luca Carettoni - eLearnSecurity](https://www.youtube.com/watch?v=yCnPMuan2fQ)
* [Quick start your Burp Suite extensions Jython and automation - Marius Nepomuceno](https://www.youtube.com/watch?v=LEkqKOijp7Q)
* [Writing a Burp Extension – Part One - Carl Sampson](https://chs.us/writing-a-burp-extension-part-one/)
* [OWASP Bay Area - Writing Burp Extensons](https://www.youtube.com/watch?v=OkQiP_Tcs68)
