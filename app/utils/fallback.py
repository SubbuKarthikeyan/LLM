from app.utils.retry import retry_request


def fallback_request(
    models,
    messages,
    retries=3,
    delay=2,
    stream=False,
    **kwargs
):
    last_error = None

    for index, model in enumerate(models):

        print("=" * 50)
        print(f"Provider : {model['name']}")
        print(f"Model    : {model['model']}")
        print(f"Fallback : {index > 0}")

        try:

            response = retry_request(
                model=model["model"],
                messages=messages,
                api_key=model["api_key"],
                retries=retries,
                delay=delay,
                stream=stream,
                **kwargs
            )

            if stream:
                return response

            return {
                    "response": response,
                    "provider": model["name"],
                    "model": model["model"],
                    "fallback": index > 0
                }

        except Exception as e:

            print(f"{model['name']} failed")
            print("Switching to next model...\n")
            print(e)

            last_error = e

    raise Exception(last_error)

    