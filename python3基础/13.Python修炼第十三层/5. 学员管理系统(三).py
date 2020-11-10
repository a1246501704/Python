\s4day67
\内容回顾：
	#1. Web框架本质
		浏览器(socket客户端):
			2. 发送IP和端口  http://www.baidu.com:80/index/
				GET:
					请求头
						http1.1 /index?p=123
						...
					请求体(无内容)	
				POST:
					请求头
						http1.1 /index?p=123
						...
					请求体
						...
			4. 接收响应
				普通响应：页面直接显示
				重定向响应：再一起一次Http请求
					
		服务器(socket服务端):
			1. 启动并监听ip和端口，等待用户连接
			3. 接收请求进行处理，并返回
				普通返回:
					响应头:
						Access-Control-Allow-Origin:*
						Cache-Control:max-age=600
						Date:Mon, 19 Jun 2017 00:57:43 GMT
						Expires:Mon, 19 Jun 2017 01:07:43 GMT
						Last-Modified:Wed, 24 May 2017 01:51:55 GMT
						Server:GitHub.com
						X-GitHub-Request-Id:C495:5EBC:8739EF:B817EE:59472187
					响应体:
						<html>
							....
						</html>
				重定向返回:
					响应头:
						LOCATION: 'http://www.baidu.com'
						Access-Control-Allow-Origin:*
						Cache-Control:max-age=600
						Date:Mon, 19 Jun 2017 00:57:43 GMT
						Expires:Mon, 19 Jun 2017 01:07:43 GMT
						Last-Modified:Wed, 24 May 2017 01:51:55 GMT
						Server:GitHub.com
						X-GitHub-Request-Id:C495:5EBC:8739EF:B817EE:59472187
	
	#2. DjangoWeb框架
		a. 创建Project
			django-admin startproject mysite

		b. 配置
			模板
			静态文件
			csrf
	
		c. 路由关系
		
			url -> 函数
			url -> 函数
			url -> 函数
			url -> 函数
			
		d. 视图函数
			def index(request):
				request.method
				request.GET.get('name')
				request.POST.get('nage')
				li = request.POST.getlist('多选下拉框name')
						
				return HttpResponse('字符串')
				return redirect('URL')
				return render(request,'模板路径',{})
				# 1. 获取模板+数据，渲染
				# 2. HttpReponse(...)
				
		c. 模板渲染
			{{k1}}
			{{k2.0}}

			{% for i in result %}
				{{i}}
			{%endfor %}
				
			{%if 1>2%}

			{%endif%}
			
			
	#3. Ajax(jQuery)
		$.ajax({
			url: '',
			type: 'GET',
			data: {k1:'v1'},
			success:function(arg){	
			}
		})

	
\今日内容：
	#1. 对话框
		单表
			添加
			编辑
			删除
			
			PS: 
				a. js阻止默认事件的发生
				b. location.reload()
				c. HttpReponse(json.dumps(xxxx))
				d. JSON.parse()
		一对多
			PS:
				a. jQuery事件阻止默认事件发生
						$('#addModal').click(function(){
							alert(123);
							return false;
						})
	#2. 多对多
		- 添加
		- 添加（左右移动）
		
	#3. Bootstrap
	
	#4. fontawesome
	
\今日任务：
	1. 上述内容
	2. 多对多添加
	3. 添加（左右移动）-可选

	
	