# coding:utf-8
import uvicorn
from fastapi import FastAPI
from test1 import main as test1
from test2 import main as test2
from test3 import main as test3
from test4 import main as test4
from test5 import main as test5
from test6 import main as test6
from test7 import main as test7
from test8 import main as test8
from test9 import main as test9
from test10 import main as test10
from test11 import main as test11
from test12 import main as test12
from test13 import main as test13
from test14 import main as test14
from test15 import main as test15
from test16 import main as test16
from test17 import main as test17
from test18 import main as test18
from test19 import main as test19
from test20 import main as test20
from test21 import main as test21
from test22 import main as test22
from test23 import main as test23
from test24 import main as test24

app = FastAPI()



@app.get("/", summary="163 MV Permanent API")
def main(vid: int = None):
    return {"hello": "world"}

@app.get("/test1")
def main1():
    return test1()

@app.get("/test2")
def main2():
    return test2()

@app.get("/test3")
def main3():
    return test3()
    
@app.get("/test4")
def main4():
    return test4()

@app.get("/test5")
def main5():
    return test5()

@app.get("/test6")
def main6():
    return test6()

@app.get("/test7")
def main7():
    return test7()
  
@app.get("/test8")
def main8():
    return test8()

@app.get("/test9")
def main9():
    return test9()
  
@app.get("/test10")
def main10():
    return test10()
  
@app.get("/test11")
def main11():
    return test11()

@app.get("/test12")
def main12():
    return test12()

@app.get("/test13")
def main13():
    return test13()
  
@app.get("/test14")
def main14():
    return test14()

@app.get("/test15")
def main15():
    return test15()

@app.get("/test16")
def main16():
    return test16()

@app.get("/test17")
def main17():
    return test17()

@app.get("/test18")
def main18():
    return test18()

@app.get("/test19")
def main19():
    return test19()

@app.get("/test20")
def main20():
    return test20()

@app.get("/test21")
def main21():
    return test21() 

@app.get("/test22")
def main22():
    return test22() 

@app.get("/test23")
def main23():
    return test23() 

@app.get("/test24")
def main24():
    return test24() 

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, log_level="info")
