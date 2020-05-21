IMAGE_NAME = yt2audio

build:
	docker build -t $(IMAGE_NAME) .

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker logs $(IMAGE_NAME)

shell:
	docker exec -it $(IMAGE_NAME) bash
