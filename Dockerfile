FROM public.ecr.aws/lambda/python:3.9

RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

CMD ["app.lambda_handler"]

EXPOSE 8083