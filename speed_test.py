import speedtest

test = speedtest.Speedtest()

print("Load list server...")
t = test.get_servers()

print(t)

# server_vn = list(filter(lambda server: server[1][0]["country"] == "South Korea", t.items()))
# print(server_vn)
print("Get best server...")
test.get_best_server(test.set_mini_server("http://owa.eastcom-sw.com:8080/speedtest/upload.php"))
# test.get_best_server(test.set_mini_server(server_vn[0][1][0].get("url")))
# best_server = test.get_best_server()
# print(best_server)

download_result = test.download()
upload_result = test.upload()
ping_result = test.results.ping

print(f"download speed : {download_result / 1024 / 1024 :.2f} Mb/sec ") # MB/second
print(f"upload speed : {upload_result / 1024 / 1024 :.2f} Mb/sec ") # MB/second
print(f"ping {ping_result :.2f} ms")



