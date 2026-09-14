import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions


def run():
    # Configuración del pipeline
    options = PipelineOptions(
        runner="DataflowRunner",  
        project="gcp-data-engineer-508502",
        region="us-central1",
        temp_location="gs://gcs-bucket-curso-508503/temp"
    )

    with beam.Pipeline(options=options) as p:
        (
            p
            | "Leer archivo" >> beam.io.ReadFromText(
                "gs://dataflow-samples/shakespeare/kinglear.txt"
            )
            | "Separar palabras" >> beam.FlatMap(
                lambda line: line.split()
            )
            | "Contar palabras" >> beam.combiners.Count.PerElement()
            | "Guardar resultados" >> beam.io.WriteToText(
                "gs://gcs-bucket-curso-508503/output/wordcount"
            )
        )


if __name__ == "__main__":
    run()