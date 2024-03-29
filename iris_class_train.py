# Databricks notebook source
  import mlflow
  import mlflow.pyfunc

  class Model(mlflow.pyfunc.PythonModel):
      def predict(self, context, model_input):
          return model_input * 2

  with mlflow.start_run():
      mlflow.pyfunc.log_model("wedata_custom_model_20240329", python_model=Model())

# COMMAND ----------


