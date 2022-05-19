import tensorflow #uses old tensorflow 1.x versions
import gpt_2_simple as gpt

gpt.download_gpt2(model_name="355M")

source_file = 'political_left.csv'

session = gpt.start_tf_sess()

gpt.fintetune(session, dataset=source_file, model_name='355M',
                steps=500, restore_from='fresh', run_name='run1',
                print_every=10, sample_every=100, save_every=1000)

gpt.generate(session, run_name='run1', nsamples=5, batch_size=5)

output_file = 'gpt_output_1.txt'

gpt.generate_to_file(session, destination_path=output_file,
                        length=1000, nsamples=100, batch_size=20)
