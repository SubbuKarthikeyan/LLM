from litellm import completion
import time


def retry_request(
    model,
    messages,
    api_key,
    retries=3,
    delay=1,
    **kwargs
):
    for attempt in range(retries):
        try:
            print(f"Model : {model}")
            print(f"Attempt : {attempt + 1}/{retries}")

            return completion(
                model=model,
                messages=messages,
                api_key=api_key,
                **kwargs
            )

        except Exception as e:
            error = str(e).lower()

            # Retry only on temporary errors
            if any(
                keyword in error
                for keyword in ["rate", "timeout", "connection", "503", "429"]
            ):
                if attempt < retries - 1:
                    print(f"Retrying... ({attempt + 1}/{retries})")
                    time.sleep(delay)
                    continue

            # Raise permanent errors immediately
            raise

    raise Exception("All retry attempts failed")