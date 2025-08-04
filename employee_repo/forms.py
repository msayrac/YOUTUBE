import inspect
from fastapi import Form


def as_form(cls):
    new_params = []

    for field_name, model_field in cls.model_fields.items():
        new_params.append(
            inspect.Parameter(
                field_name,
                inspect.Parameter.POSITIONAL_OR_KEYWORD,
                default = Form(...) if model_field.is_required() else Form(model_field.default),
                annotation = model_field.annotation,
            )
        )





