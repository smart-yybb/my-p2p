import argparse
import os
import torch
import time
from diffusers import DDIMScheduler

from p2p import Editor, CrossAttnCtrl
from utils import image_grid

parser = argparse.ArgumentParser()
parser.add_argument('--device', type=str, default='cuda')
parser.add_argument('--model_id', type=str,
                    default='./models--runwayml--stable-diffusion-v1-5/snapshots/1d0c4ebf6ff58a5caecab40fa1406526bca4b5b9')
parser.add_argument('--prompt', type=str, default='A nigger with a woman.')
parser.add_argument('--num_inference_steps', type=int, default=50)

args = parser.parse_args()
device = args.device
model_id = args.model_id
prompt = args.prompt
steps = args.num_inference_steps
result_path = './result'

ddim_scheduler = DDIMScheduler.from_pretrained(model_id,
                                               subfolder="scheduler",
                                               local_files_only=True)
SD = Editor.from_pretrained(
    model_id, scheduler=ddim_scheduler, torch_dtype=torch.float32,
    cache_dir='.', processor=CrossAttnCtrl(),
).to(device)
generator = torch.Generator(device).manual_seed(20231102)

os.makedirs(result_path, exist_ok=True)

start = time.time()
count = 0
with open('./prompts.txt') as file:
    lines = file.readlines()
    for prompt_target in lines:
        count += 1
        print("【Generating the {}th prompts' picture...】".format(count))
        images = SD(
            prompt=prompt, prompt_target=prompt_target,
            generator=generator, num_inference_steps=steps,
        ).images
        image = image_grid(images, rows=1, cols=2)
        image.save('{}/prompt-{}.png'.format(result_path, count))
end = time.time()
print('【Completed to generate {} pictures, cost:{}s】'.format(count, round(end - start)))
