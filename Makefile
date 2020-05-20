build:
	docker build -t yt2audio .

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker logs yt2audio

shell:
	docker exec -it yt2audio bash
