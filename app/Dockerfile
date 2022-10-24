# pull the official base image
FROM python:3.8-slim-buster

# set working direction
WORKDIR /app
ENV port=4000
# add app
COPY *.py ./.

# RUN chown -R 1000:1000 ./
USER 1000
#The EXPOSE instruction does not actually publish the port. It functions as a type of documentation between the person who builds the image and the person who runs the containe
EXPOSE 4000
# start app
CMD ["python3", "server-multiprocessing.py"]

