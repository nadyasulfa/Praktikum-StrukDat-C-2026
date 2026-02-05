tim_frontend = {"HTML", "CSS", "JavaScript", "Reatct"}
tim_backend = {"Python", "JavaScript", "SQL", "NodeJS"}

set3 = tim_frontend.intersection(tim_backend)
print(set3)

set3 = tim_backend.difference(tim_frontend)
print(set3)

set3 = tim_frontend | tim_backend
print(set3)