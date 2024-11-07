# LiteLLM

- https://www.litellm.ai/

> LLM Gateway to manage authentication, loadbalancing, and spend tracking across 100+ LLMs. All in the OpenAI format.

- Git Repo: https://github.com/BerriAI/litellm

> Python SDK, Proxy Server (LLM Gateway) to call 100+ LLM APIs in OpenAI format - [Bedrock, Azure, OpenAI, VertexAI, Cohere, Anthropic, Sagemaker, HuggingFace, Replicate, Groq]

- Document: https://docs.litellm.ai/docs/

## 2024-11-07

- ( 2024-11-07 09:50:02 )
- Installation
  - 測試環境：Github Codespace
```bash
jazzw@JazzBook:~/git/snippet/python/litellm$ gh cs ssh
? Choose codespace: jazzwang/snippet (master*): snippet
Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 6.5.0-1025-azure x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro
Last login: Wed Nov  6 14:20:47 2024 from ::1
@jazzwang ➜ /workspaces/snippet (master) $
@jazzwang ➜ /workspaces/snippet (master) $ pip3 install litellm
Collecting litellm
@jazzwang ➜ /workspaces/snippet (master) $ which litellm
/home/codespace/.python/current/bin/litellm
@jazzwang ➜ /workspaces/snippet (master) $ litellm
Traceback (most recent call last):
  File "/home/codespace/.python/current/lib/python3.10/site-packages/litellm/proxy/proxy_server.py", line 58, in <module>
    import backoff
ModuleNotFoundError: No module named 'backoff'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/codespace/.python/current/bin/litellm", line 8, in <module>
    sys.exit(run_server())
  File "/home/codespace/.python/current/lib/python3.10/site-packages/click/core.py", line 1157, in __call__
    return self.main(*args, **kwargs)
  File "/home/codespace/.python/current/lib/python3.10/site-packages/click/core.py", line 1078, in main
    rv = self.invoke(ctx)
  File "/home/codespace/.python/current/lib/python3.10/site-packages/click/core.py", line 1434, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/home/codespace/.python/current/lib/python3.10/site-packages/click/core.py", line 783, in invoke
    return __callback(*args, **kwargs)
  File "/home/codespace/.python/current/lib/python3.10/site-packages/litellm/proxy/proxy_cli.py", line 289, in run_server
    raise e
  File "/home/codespace/.python/current/lib/python3.10/site-packages/litellm/proxy/proxy_cli.py", line 275, in run_server
    from .proxy_server import (
  File "/home/codespace/.python/current/lib/python3.10/site-packages/litellm/proxy/proxy_server.py", line 64, in <module>
    raise ImportError(f"Missing dependency {e}. Run `pip install 'litellm[proxy]'`")
ImportError: Missing dependency No module named 'backoff'. Run `pip install 'litellm[proxy]'`
@jazzwang ➜ /workspaces/snippet (master) $ pip install 'litellm[proxy]'
@jazzwang ➜ /workspaces/snippet (master) $ litellm --help
Usage: litellm [OPTIONS]

Options:
  --host TEXT                Host for the server to listen on.
  --port INTEGER             Port to bind the server to.
  --num_workers INTEGER      Number of gunicorn workers to spin up
  --api_base TEXT            API base URL.
  --api_version TEXT         For azure - pass in the api version.
  -m, --model TEXT           The model name to pass to litellm expects
  --alias TEXT               The alias for the model - use this to give a
                             litellm model name (e.g.
                             "huggingface/codellama/CodeLlama-7b-Instruct-hf")
                             a more user-friendly name ("codellama")
  --add_key TEXT             The model name to pass to litellm expects
  --headers TEXT             headers for the API call
  --save                     Save the model-specific config
  --debug                    To debug the input
  --detailed_debug           To view detailed debug logs
  --use_queue                To use celery workers for async endpoints
  --temperature FLOAT        Set temperature for the model
  --max_tokens INTEGER       Set max tokens for the model
  --request_timeout INTEGER  Set timeout in seconds for completion calls
  --drop_params              Drop any unmapped params
  --add_function_to_prompt   If function passed but unsupported, pass it as
                             prompt
  -c, --config TEXT          Path to the proxy configuration file (e.g.
                             config.yaml). Usage `litellm --config
                             config.yaml`
  --max_budget FLOAT         Set max budget for API calls - works for hosted
                             models like OpenAI, TogetherAI, Anthropic, etc.`
  --telemetry BOOLEAN        Helps us know if people are using this feature.
                             Turn this off by doing `--telemetry False`
  --log_config TEXT          Path to the logging configuration file
  -v, --version              Print LiteLLM version
  --health                   Make a chat/completions request to all llms in
                             config.yaml
  --test                     proxy chat completions url to make a test request
                             to
  --test_async               Calls async endpoints /queue/requests and
                             /queue/response
  --iam_token_db_auth        Connects to RDS DB with IAM token
  --num_requests INTEGER     Number of requests to hit async endpoint with
  --run_gunicorn             Starts proxy via gunicorn, instead of uvicorn
                             (better for managing multiple workers)
  --run_hypercorn            Starts proxy via hypercorn, instead of uvicorn
                             (supports HTTP/2)
  --ssl_keyfile_path TEXT    Path to the SSL keyfile. Use this when you want
                             to provide SSL certificate when starting proxy
  --ssl_certfile_path TEXT   Path to the SSL certfile. Use this when you want
                             to provide SSL certificate when starting proxy
  --local                    for local debugging
  --help                     Show this message and exit.
```