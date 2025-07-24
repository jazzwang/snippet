import argparse
from dia.model import Dia

def main():
    parser = argparse.ArgumentParser(description="Generate audio from text using the Dia model.")
    parser.add_argument("input_text_file", type=str, help="Path to the input text file.")
    parser.add_argument("output_mp3_file", type=str, help="Path to save the output MP3 file.")
    
    args = parser.parse_args()
    
    model = Dia.from_pretrained("nari-labs/Dia-1.6B-0626", compute_dtype="float16")
    
    with open(args.input_text_file, 'r', encoding='utf-8') as file:
        text = file.read().strip()
    
    output = model.generate(
        text,
        use_torch_compile=False,
        verbose=True,
        cfg_scale=3.0,
        temperature=1.8,
        top_p=0.90,
        cfg_filter_top_k=50,
    )
    
    model.save_audio(args.output_mp3_file, output)

if __name__ == "__main__":
    main()