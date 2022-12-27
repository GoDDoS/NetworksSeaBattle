FROM python:latest

RUN apt-get install tk -y

ADD run.py /Client/
ADD result_view.py /Client/
ADD view_factory.py /Client/
ADD server_listener.py /Client/
ADD menu_view.py /Client/
ADD game_view.py /Client/
ADD BaseView.py /Client/
ADD error_view.py /Client/

WORKDIR /Client/
