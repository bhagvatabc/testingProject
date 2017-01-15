import os,json
from flask import Flask, render_template, request
from werkzeug import secure_filename
from database import connection
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploaded_files'
@app.route('/')
def upload_file():
   
   return render_template('uploadfile.html')
@app.route('/uploader', methods = ['POST'])
def upload_file1():
   if request.method == 'POST':
    	f = request.files['file']
    	nameOfFile = str(f.filename)
      	print f
      	try:
        	c, conn = connection()
        	f.save(os.path.join(app.config['UPLOAD_FOLDER'], nameOfFile))
        	# sqlquery = ("select * from filestore2")
        	# c.execute(sqlquery)
        	# rows = c.fetchall()
        	# print rows
        	query="""insert filestore2(f_name) values (%s)"""
        	c.execute(query,[nameOfFile])
        	conn.commit()
        	c.close()
        	conn.close()
        	result = getAllFiles()
        	return render_template('uploaded.html',data=result)

        except Exception as e:
        	print "inside exe"
        	return(str(e))

def getAllFiles():
    print "inside get_All_Files"
    allFiles = []
    try:
        c, conn = connection()
        sqlquery = ("select f_name from filestore2")
        c.execute(sqlquery)
        rows = c.fetchall()
        
        res_list = [x[0] for x in rows]
        
        for name in res_list:
          file_name1 = {'name':name}
          allFiles.append(file_name1)
        
        print allFiles 
        conn.commit()
        c.close()
        conn.close()
        return (allFiles)
    except Exception as e:
        print "inside exe getAllFiles"
        print (str(e))
        return(str(e))
      	
if __name__ == '__main__':
   app.run(debug = True)