# Filed-Audio-server

1. Check requirements.txt, If needed Install requirements accordingly.
2. Need to create a blank MySql database With name audio_project
3. change Database port, User, Pasword according to yours. folder path :- [DRIVE:]\audio_server_debapriya_palai\audio_project\audio_project\settings.py > line no:79-85
4. open cmd in [DRIVE:]\audio_server_debapriya_palai\audio_project
Run commands in cmd to start server: 
					python manage.py makemigrations
					python manage.py migrate
					python populate_audio.py
					python manage.py runserver
					
					
					
Api Endpoints:

http://127.0.0.1:8000/song - GET: all songs
							               POST : add new song

http://127.0.0.1:8000/song/{id} - GET: particular song details
							                    PUT : update particular song details
								                  DELETE : delete particular song
								  
--------------------------------------------------------------------------------------							 
							 
http://127.0.0.1:8000/podcast - GET: all podcast
							                  POST : add new podcast
								
http://127.0.0.1:8000/podcast/{id} - GET: particular podcast details
							                       PUT : update particular podcast details
								                     DELETE : delete particular podcast								
								
--------------------------------------------------------------------------------------
								
http://127.0.0.1:8000/audiobook - GET: all audiobooks
							                    POST : add new audiobook
								  
http://127.0.0.1:8000/audiobook/{id}  - GET: particular audiobook details
							                          PUT : update particular audiobook details
								                        DELETE : delete particular audiobook
