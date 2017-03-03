function out = extensionPrinciple(A,B,operator)
% out = extensionPrinciple(A,B,operator)
% Function to compute math operations on fuzzy sets using extension
% principle. Also plots the output
% A,B = 2 column matrix, with col 1 = domain & col 2 = fuzzy set
% operator = 'sum','sub','mul','div','max','min','exp'
% out = output fuzzy set, with col 1 as the domain.

% Example:
% A = 0:0.1:1;
% A(2,:) = trimf(A(1,:),[0.1,0.4,0.7]);
% B = 0:0.05:1;
% B(2,:) = trapmf(B(1,:),[0.2,0.4,0.7,0.9]);
% out = extensionPrinciple(A,B,'sum')
    % Output holder
    out = [];
    % index of the output
    n = 1;
    for i = 1:size(A,2)
        for j = 1:size(B,2)
            % Perform the operation for each combination of domain of A and B.
            % x # y from Keller's book. The operation is only carried out
            % between domains, not the fuzzy set membership values.
            switch operator
                case 'sum'
                    % my_round function is just to avoid Matlab from
                    % producing goofy outputs.
                    z = my_round((A(1,i) + B(1,j)));
                case 'sub'
                    z = my_round((A(1,i) - B(1,j)));
                case 'mul'
                    z = my_round((A(1,i) * B(1,j)));
                case 'div'
                    if(B(1,j) ~= 0)
                        z = my_round((A(1,i) / B(1,j)));
                    else z = 0;
                    end
                case 'max'
                    z = my_round(max(A(1,i),B(1,j)));
                case 'min'
                    z = my_round(min(A(1,i), B(1,j)));
                case 'exp'
                    z = my_round((A(1,i)^B(1,j)));
                otherwise
                    warning('Unexpected operator');
            end
            % Take min of both the dimensions
            f = min(A(2,i),B(2,j));
            % If this output domain value has occured before, then find it's
            % index and take the max with whatever value we already have.
            if(~isempty(out)), idx = find(out(1,:) == z);
            else idx = 0;
            end

            if(idx)
                out(2,idx) = max(out(2,idx),f);
            % if this output domain value hasn't occured before, then add a new
            % column to the output and increament the counter.
            else
                out(:,n) = [z;f];
                n = n + 1;
            end
        end
    end
    % sort the domain of the output.
    [~,fooi] = sort(out(1,:),'ascend');
    out = out(:,fooi);
    plot(A(1,:),A(2,:),'k.-')
    hold on;
    plot(B(1,:),B(2,:),'b.-')
    plot(out(1,:),out(2,:),'r.-')
    legend({'input 1','input 2',operator});
    hold off;
end

function rounded = my_round(in, varargin)
    if(nargin == 1)
        roundtoDigits = 2;
    else
        roundtoDigits = varargin{1};
    end
    rounded = (round(in*(10^roundtoDigits)))/(10^roundtoDigits);
end

