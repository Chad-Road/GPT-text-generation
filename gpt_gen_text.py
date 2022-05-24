import tensorflow #uses old tensorflow 1.x versions
import gpt_2_simple as gpt

def generate_text(source_file, output_file, model_name="355M"):

    # Initialize model and choose what complexity of model you want to choose: 124M, 355M, 774M
    gpt.download_gpt2(model_name=model_name)

    # Select file location and name used for model training
    source_file = source_file

    # Start a new session and train of source text
    session = gpt.start_tf_sess()
    gpt.fintetune(session, dataset=source_file, model_name=model_name,
                    steps=500, restore_from='fresh', run_name='run1',
                    print_every=10, sample_every=100, save_every=1000)

    # Below code can be uncommented to generate sample for quality checking
    # gpt.generate(session, run_name='run1', nsamples=5, batch_size=5)

    # Output file name and parameters for generated text
    output_file = output_file
    gpt.generate_to_file(session, destination_path=output_file,
                            length=1000, nsamples=100, batch_size=20)

if __name__ == '__main__':
    generate_text("source file", "output file name")
